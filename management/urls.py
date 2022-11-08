from django.urls import path
from .views import index, add_report, out

urlpatterns = [
    path('', index),
    path('add-report/', add_report),
    path('send-report/', out),
]
