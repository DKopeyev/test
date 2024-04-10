from django.shortcuts import render
from .models import Trainer,Gym,Schedule

# Create your views here.


def trainer_list(request):
    """
    Отображает список тренеров.

    Args:
        request (HttpRequest): HTTP запрос.

    Returns:
        HttpResponse: HTTP ответ с отображением шаблона списка тренеров.

    Пример использования:
        # Для отображения списка тренеров
        return trainer_list(request)
    """
    trainers = Trainer.objects.all()

    context = {
        'trainers': trainers
    }

    return render(request, 'trainer_list.html', context)



def schedule(request):
    """
    Отображает расписание тренеров.

    Args:
        request (HttpRequest): HTTP запрос.

    Returns:
        HttpResponse: HTTP ответ с отображением шаблона расписания.


    Пример использования:
        # Для отображения расписания тренеров
        return schedule_view(request)
    """
   
    schedules = Schedule.objects.all()

    context = {'schedules': schedules}

    return render(request, 'schedule.html', context)


def gyms(request):
    """
        Отображает список залов фитнеса.

        Args:
            request (HttpRequest): HTTP запрос.

        Returns:
            HttpResponse: HTTP ответ с отображением шаблона списка залов фитнеса.

        Пример использования:
            # Для отображения списка залов фитнеса
            return gyms(request)
    """
    gyms = Gym.objects.all()

    context = {
        'gyms':gyms
    }

    return render(request,'gyms.html', context)


