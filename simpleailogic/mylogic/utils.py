from datetime import datetime
from datetime import timedelta
import os
from django.conf import settings
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
    # Fetch user data
    apple_health_stat = AppleHealthStat.objects.filter(user=user).last()
    
    # Create prompt for OpenAI API
    prompt = f"Provide advice for a user with the following data: {apple_health_stat}"
    
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    print(completion.choices[0].message)

    answer = completion.choices[0].message
    
    return answer