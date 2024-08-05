from rest_framework import serializers
from django.contrib.auth.models import User
from mylogic.models import AppleHealthStat

class AppleHealthStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppleHealthStat
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
