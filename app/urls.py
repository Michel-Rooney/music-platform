from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_music/<str:id>/', views.add_music, name='add_music'),
    path('delete_music/<str:id>/', views.delete_music, name='delete_music'),
]