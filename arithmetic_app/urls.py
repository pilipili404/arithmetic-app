# arithmetic_app/urls.py
from django.urls import path
from .views import ArithmeticArrangerView

urlpatterns = [
    path('arrange/', ArithmeticArrangerView.as_view(), name='arithmetic-arrange'),
]


