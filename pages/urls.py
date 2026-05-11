from django.urls import path
from .import views

app_name = 'xxxx'

urlpatterns = [
    path('',views.index, name='index'),

]