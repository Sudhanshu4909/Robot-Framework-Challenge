# robot_challenge_project/urls.py
from django.urls import path
from api.views import execute_tests

urlpatterns = [
    path('testai/tests/v1/execute', execute_tests, name='execute_tests'),
]
