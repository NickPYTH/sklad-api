from django.urls import path

from .views import generate_user_report_xlsx, generate_second_report_xlsx

urlpatterns = [
    path('report/', generate_user_report_xlsx),
    path('report2/', generate_second_report_xlsx),
]
