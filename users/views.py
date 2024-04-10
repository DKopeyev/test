from django.shortcuts import render
from .models import User

# Create your views here.



def user_list(request):
    """
    Представление для отображения списка всех пользователей.

    Args:
        request: Объект запроса Django.

    Returns:
        HTTP-ответ с отображением списка всех пользователей.
    """

    users = User.objects.all()

    context = {
        'users': users
    }
    return render(request, 'user_list.html', context)