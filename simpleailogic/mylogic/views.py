import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AppleHealthStat
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
import os
from django.conf import settings
from openai import OpenAI
from django.db.models import Sum
from .utils import get_week_date_range, generate_ai_response
from dotenv import load_dotenv

# openai.api_key = settings.OPENAI_API_KEY
os.environ['OPENAI_API_KEY'] = settings.OPENAI_API_KEY

class HealthConditionsAPIView(APIView):
    def get(self, request):
        User = get_user_model()
        
        print("User All", User.objects.all())
        # Get users with total sleep time condition
        sleep_condition_users = filter_users_by_sleep_condition()
        print("Sleep", sleep_condition_users)
        
        
        # Get users who walked less than 5000 steps
        step_1_condition_users = User.objects.filter(
            apple_health_stat__stepCount__lt=5000
        ).distinct()

        print("Step 1", step_1_condition_users)
        
        # Get users who walked 50% less this week compared to the previous week
        step_2_condition_users = filter_users_by_step_decrease()
        
        print("Step 2", step_2_condition_users)
        
        # Combine conditions
        combined_users = set(sleep_condition_users) & set(step_1_condition_users) & set(step_2_condition_users)
        
        print("Combined", combined_users)
        # Generate response
        response_data = []
        for user in combined_users:
            ai_response = generate_ai_response(user)
            response_data.append({
                "user": user.username,
                "ai_response": ai_response
            })
        
        return Response(response_data)

def filter_users_by_sleep_condition():
    """Filters users based on total sleep time across all sleep sessions."""
    User = get_user_model()
    users_with_short_sleep = []

    # Iterate over all users
    for apple_health_stat in AppleHealthStat.objects.all():
        sleep_analysis_data = apple_health_stat.sleepAnalysis
        total_sleep_time = sum(item.get('sleep_time', 0) for item in sleep_analysis_data) if sleep_analysis_data else 0
        
        # Check if total sleep time is less than 12 hours (43200 seconds)
        if total_sleep_time < 21600:
            users_with_short_sleep.append(apple_health_stat.user)

    return User.objects.filter(id__in=[user.id for user in users_with_short_sleep]).distinct()

def filter_users_by_step_decrease():
    """Filters users who walked 50% less this week compared to the previous week."""
    User = get_user_model()
    
    # Get date ranges for current and previous weeks
    current_week_start, current_week_end = get_week_date_range(0)
    previous_week_start, previous_week_end = get_week_date_range(-1)
    
    print("dates", current_week_start, current_week_end, previous_week_start, previous_week_end)

    # Calculate steps for current and previous weeks
    current_week_steps = AppleHealthStat.objects.filter(
        created_at__range=(current_week_start, current_week_end)
    ).values('user').annotate(total_steps=Sum('stepCount'))

    previous_week_steps = AppleHealthStat.objects.filter(
        created_at__range=(previous_week_start, previous_week_end)
    ).values('user').annotate(total_steps=Sum('stepCount'))
    
    print("data", current_week_steps)
    previous_week_steps = current_week_steps
    print("previous", previous_week_steps)

    previous_week_steps_dict = {stat['user']: stat['total_steps'] for stat in previous_week_steps}
    
    print("stats", previous_week_steps)
    
    step_decrease_users = []
    for stat in current_week_steps:
        user_id = stat['user']
        current_steps = stat['total_steps'] or 0
        previous_steps = previous_week_steps_dict.get(user_id, 0)
        
        if previous_steps > 0:  # Avoid division by zero
            percentage_decrease = ((previous_steps - current_steps) / previous_steps) * 100
            if percentage_decrease >= 0:
                user = User.objects.get(id=user_id)
                step_decrease_users.append(user)
    
    return step_decrease_users
