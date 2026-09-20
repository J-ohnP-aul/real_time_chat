from django.urls import path

from . import views

urlpatterns = [
  path('', views.rooms_v, name='rooms'),
  path('<slug:slug>', views.room_v, name='room'),

]
