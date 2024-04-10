from django.contrib import admin
from booking.models import Booking


# admin.site.register(Booking)
@admin.register(Booking)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('client', 'trainer', 'date' , 'hall', 'start_time')