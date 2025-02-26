# Generated by Django 5.0.7 on 2024-08-05 11:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppleHealthStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfBirth', models.DateTimeField(blank=True, null=True)),
                ('height', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('bodyMass', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('bodyFatPercentage', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('biologicalSex', models.CharField(blank=True, max_length=32, null=True)),
                ('activityMoveMode', models.CharField(blank=True, max_length=128, null=True)),
                ('stepCount', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('basalEnergyBurned', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('activeEnergyBurned', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('flightsClimbed', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('appleExerciseTime', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('appleMoveTime', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('appleStandHour', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('menstrualFlow', models.CharField(blank=True, max_length=128, null=True)),
                ('HKWorkoutTypeIdentifier', models.CharField(blank=True, max_length=128, null=True)),
                ('heartRate', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('oxygenSaturation', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('mindfulSession', models.JSONField(blank=True, null=True)),
                ('sleepAnalysis', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apple_health_stat', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
