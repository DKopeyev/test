from django.db import models
from trainers.models import Trainer,Gym
from users.models import User
# Create your models here.

class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    hall = models.ForeignKey(Gym, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()

   
