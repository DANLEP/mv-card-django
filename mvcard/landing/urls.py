from django.urls import path

from landing.views import LandingHome

urlpatterns = [
    path('', LandingHome.as_view(), name='home'),
]