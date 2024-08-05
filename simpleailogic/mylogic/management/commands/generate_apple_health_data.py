from django.core.management.base import BaseCommand
from mylogic.models import AppleHealthStat
from django.contrib.auth import get_user_model
from faker import Faker
import random
import datetime

class Command(BaseCommand):
    help = 'Generate random Apple Health data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        User = get_user_model()
        users = User.objects.all()
        print("users", users)
        for user in users:
            AppleHealthStat.objects.create(
                user=user,
                dateOfBirth=fake.date_of_birth(),
                height=random.randint(150, 200),
                bodyMass=random.randint(50, 100),
                bodyFatPercentage=random.randint(10, 40),
                biologicalSex=random.choice(['male', 'female']),
                activityMoveMode=random.choice(['activeEnergy', 'stepCount']),
                stepCount=random.randint(1000, 10000),
                basalEnergyBurned=random.randint(1000, 2000),
                activeEnergyBurned=random.randint(100, 500),
                flightsClimbed=random.randint(0, 10),
                appleExerciseTime=random.randint(0, 60),
                appleMoveTime=random.randint(0, 60),
                appleStandHour=random.randint(0, 12),
                menstrualFlow=random.choice(['low', 'medium', 'high', 'unspecified']),
                HKWorkoutTypeIdentifier=random.choice(['running', 'cycling', 'swimming', 'walking']),
                heartRate=random.randint(50, 100),
                oxygenSaturation=random.randint(95, 100),
                mindfulSession={},
                sleepAnalysis = [{
                        "date": (datetime.datetime.now() - datetime.timedelta(
                            days=random.randint(0, 5 * 7), 
                            minutes=random.randint(0, 1440)
                        )).strftime("%Y-%m-%d %H:%M"),
                        "sleep_time": random.randint(300, 28800)
                    } for _ in range(5 * 7)],
            )
            
            
