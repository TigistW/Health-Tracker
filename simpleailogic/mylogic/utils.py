from collections import defaultdict
from datetime import datetime
from datetime import timedelta
import os
from django.conf import settings
import openai
from .models import AppleHealthStat
from openai import OpenAI

# openai.api_key = settings.OPENAI_API_KEY
os.environ['OPENAI_API_KEY'] = settings.OPENAI_API_KEY

def get_week_date_range(week_offset=0):
    """ Returns the start and end date of the week with offset. 0 for current week, -1 for previous week. """
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    start_date = start_of_week + timedelta(weeks=week_offset)
    end_date = start_date + timedelta(days=6)
    return start_date, end_date


def generate_ai_response(user):
    analysis = generate_analysis(user)
    if not analysis:
        return "I couldn't find any data to analyze for you."

    sleep_data = analysis['sleep_by_date']
    step_data = analysis['step_data']

    # Prepare prompt for OpenAI
    avg_sleep = sum(sleep_data.values()) / len(sleep_data) if sleep_data else 0
    prompt = f"Hello, {user.username}. Based on your recent health data, you have been sleeping an average of {avg_sleep / 3600:.2f} hours per night."

    if step_data:
        prompt += f" You walked a total of {step_data} steps recently. "

    prompt += "Provide personalized advice to help the user improve their health based on this data."

    client = OpenAI()
    
    print(prompt)

    # Call OpenAI API
    try:
        print("in try")
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        print(completion.choices[0].message)

        advice = completion.choices[0].message
        
    except Exception as e:
        advice = f"An error occurred while generating advice: {str(e)}"
    
    return advice
# Utility functions for analysis
def organize_sleep_data(sleep_data):
    sleep_by_date = defaultdict(int)
    for entry in sleep_data:
        date_str = entry['date'].split()[0]  # Extract the date part (YYYY-MM-DD)
        sleep_time = entry['sleep_time']
        sleep_by_date[date_str] += sleep_time
    return sleep_by_date

def generate_analysis(user):
    apple_health_stat = AppleHealthStat.objects.filter(user=user).last()
    if not apple_health_stat:
        return None

    # Organize sleep data
    sleep_data = apple_health_stat.sleepAnalysis
    sleep_by_date = organize_sleep_data(sleep_data)

    # Analyze step count data
    step_data = apple_health_stat.stepCount

    analysis = {
        'sleep_by_date': sleep_by_date,
        'step_data': step_data,
    }
    
    return analysis
