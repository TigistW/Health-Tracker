from django.urls import path
from .views import HealthConditionsAPIView

urlpatterns = [
    path('api/health-stats/', HealthConditionsAPIView.as_view(), name='health-stats'),
]
