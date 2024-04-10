from django.urls import path
from trainers import views

app_name = 'trainers'

urlpatterns = [
    path('', views.trainer_list, name='trainer'),
    path('schedule/', views.schedule, name='schedule'),
    path('gyms/', views.gyms, name='gym'),
]