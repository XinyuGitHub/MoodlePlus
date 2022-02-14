import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'MoodlePlus.settings')

import django

django.setup()
from Demo.models import *


def populate_time_period():
    days = [TimePeriod.MON, TimePeriod.TUE, TimePeriod.WED, TimePeriod.THU, TimePeriod.FRI]
    for day in days:
        for time in range(9, 18):
            t = TimePeriod.objects.get_or_create(day=day, time=time)[0]
            t.save()


def populate_user():
    student_usernames = ['Jack', 'Emily']
    professor_usernames = ['Harry', 'Charlotte']
    # passwords = ['Jack123','Harry123','Emily123','Charlotte123']
    for name in student_usernames:
        t = User.objects.get_or_create(username=name)[0]
        t.email = name + '@student.gla.ac.uk'
        t.is_staff = False
        t.set_password(name + '123')
        t.save()

    for name in professor_usernames:
        t = User.objects.get_or_create(username=name)[0]
        t.email = name + '@student.gla.ac.uk'
        t.is_staff = True
        t.set_password(name + '123')
        t.save()




def populate():
    populate_time_period()
    populate_user()


if __name__ == '__main__':
    print('Starting MoodlePlus population script...')
    populate()
