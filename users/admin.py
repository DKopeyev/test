from django.contrib import admin

from .models import User
# Register your models here.



@admin.register(User)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('username','first_name', 'last_name','role',)