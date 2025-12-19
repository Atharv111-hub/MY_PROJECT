from django.urls import path
from . import views


app_name = 'mainapp'


urlpatterns = [
path('', views.landing, name='landing'),
path('api/contact/', views.submit_contact, name='submit_contact'),
path('api/subscribe/', views.subscribe, name='subscribe'),
]