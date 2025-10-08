# Django modules
from django.contrib import admin
from django.urls import path
from apps.tasks import views 

# Project modules
from apps.tasks.views import hello_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #path(route="hello/", view=hello_view, name="hello-view"),
    #path('', hello_view, name='home'),
    path("", views.welcome, name="welcome"),
    path("users/", views.users, name="users"),
    path("city-time/", views.city_time, name="city_time"),
    path("cnt/", views.counter, name="counter"),

]
