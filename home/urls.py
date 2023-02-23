from django.urls import path
from .views import index_page

app_name = 'home'

urlpatterns = [
    path('', index_page, name='home_page'),
]