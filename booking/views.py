from django.shortcuts import render
from .models import Booking

# Create your views here.

def booking_list(request):
    """
    Отображает список всех бронирований.

    Args:
        request (HttpRequest): HTTP запрос.

    Returns:
        HttpResponse: HTTP ответ с отображением шаблона списка бронирований.

    Пример использования:
        # Для отображения списка бронирований
        return booking_list(request)
    """
    bookings = Booking.objects.all()

    context = {
        'bookings': bookings
    }

    return render(request, 'booking_list.html', context)