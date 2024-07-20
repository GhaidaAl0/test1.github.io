from django.contrib import admin
from django.urls import path

from techapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path("index/", views.hello, name='index'),
    path('room/<str:keycard_id>/', views.room, name='room'),
]
