from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome, name = "welcome"),
    path("api/", views.member_list, name="member-list"),
]