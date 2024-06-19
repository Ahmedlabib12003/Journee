from django.urls import path
from . import views

app_name = "travel_plan"
urlpatterns = [
    path("", views.booking, name="booking"),
    
]