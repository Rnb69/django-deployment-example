from django.urls import path
from django.conf.urls import url
from basic_app import views

#TEMPLATES URLs
app_name = 'basic_app'

urlpatterns = [
    path('register/',views.register,name='register')
]
