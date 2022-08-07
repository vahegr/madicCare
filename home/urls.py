from django.urls import path
from .views import HomePage

app_name = 'home'

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
]