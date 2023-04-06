from dateutil.relativedelta import relativedelta
from django.utils import timezone


def get_datetime():
    return timezone.now()


def age(date):
    # Get the current date
    now = get_datetime()
    now = now.date()

    return relativedelta(now, date).years
