from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'), # http://127.0.0.1:8000/report
    path('month/<int:monthid>/', month), # http://127.0.0.1:8000/report/month
]