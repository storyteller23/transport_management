from django.urls import path
from .views import home, ReportCreateView, reports_view

urlpatterns = [
    path('', home, name='homepage'),
    path('send_report/', ReportCreateView.as_view(), name='send_report'),
    path('check_reports/', reports_view, name='check_reports'),
]
