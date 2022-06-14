# Go to main project and include the app in main urls.py.

from django.urls import path, include

urlpatterns = [
    path('university', include('university.urls')),
]