from django.urls import path, include

from authentication.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/done/', LoginView.as_view(), name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),
]
