from django.db import models
from users.models import User

# Create your models here.

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null = False, verbose_name= "Полное имя" )
    birth_date = models.DateField(verbose_name= "Дата рождения")
    gender = models.CharField(max_length=10,verbose_name= "Пол" )
    halls = models.ManyToManyField('Gym',verbose_name= "Зал")
    
    def __str__(self) -> str:
        return self.full_name
    

class Gym(models.Model):
    name = models.CharField(max_length=15, verbose_name= "Название зала")

    def __str__(self) -> str:
        return self.name

class Schedule(models.Model):
    DAYS = (
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
        ('Saturday', 'Суббота'),
        ('Sunday', 'Воскресенье'),
    )
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    hall = models.ForeignKey(Gym, on_delete=models.CASCADE)
    day = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField(default='22:00:00')

    def __str__(self):
        return f"{self.trainer} - {self.hall} - {self.day} - {self.start_time} - {self.end_time}"
