from django.contrib import admin

from trainers.models import Trainer,Gym, Schedule
from .forms import ScheduleAdminForm


admin.site.register(Gym)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    form = ScheduleAdminForm


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'gender' )


