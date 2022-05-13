from django.urls import path

from personal_account.views import *

urlpatterns = [
    path('', ApplicationsListView.as_view(), name='account'),
    path('history/', ApplicationsHistoryListView.as_view(), name='app-history'),
    path('accept/<int:id>', accept_application, name='app-accept'),
    path('decline/<int:id>', decline_application, name='app-decline'),
]