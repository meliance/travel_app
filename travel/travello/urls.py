from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_trip/', views.search_trip, name='search_trip'),  # Add this line
]
