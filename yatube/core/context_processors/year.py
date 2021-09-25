import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    date_now = datetime.datetime.now()
    date_obj = int(date_now.strftime('%Y'))

    return {
        'year': date_obj
    }
