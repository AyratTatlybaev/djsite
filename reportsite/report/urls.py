from django.urls import path

from .views import *

urlpatterns = [
    path('', index), # http://127.0.0.1:8000/report
    path('month/<int:month_id>/', month), # http://127.0.0.1:8000/report/month
]