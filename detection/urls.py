from django.urls import path
from .views import detect_acne

urlpatterns = [
    path('', detect_acne, name='detect_acne'),
]
