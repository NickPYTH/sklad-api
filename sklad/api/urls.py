from django.urls import path

from .views import generate_user_report_xlsx

urlpatterns = [
    path('report/', generate_user_report_xlsx),
]
