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

    populate_professor(professor_usernames)
    populate_course()
    populate_student(student_usernames)


def populate_student(student_usernames):
    for name in student_usernames:
        t = Student.objects.get_or_create(user=User.objects.get(username=name))[0]
        t.save()


def populate_professor(professor_usernames):
    for name in professor_usernames:
        t = Professor.objects.get_or_create(user=User.objects.get(username=name))[0]
        t.save()


def populate_course():
    courses = [
        {'name': 'course A', 'prerequisites': [], 'time_period': [(TimePeriod.MON, 9)], 'professor': 'Harry'},
        {'name': 'course B', 'prerequisites': [], 'time_period': [(TimePeriod.MON, 10),(TimePeriod.TUE, 10)], 'professor': 'Harry'},
        {'name': 'course C', 'prerequisites': ['course B'], 'time_period': [(TimePeriod.MON, 11)], 'professor': 'Charlotte'},
        {'name': 'course C Hard', 'prerequisites': ['course C','course A'], 'time_period': [(TimePeriod.MON, 10)],
         'professor': 'Charlotte'},
    ]
    for course in courses:
        t = Course.objects.get_or_create(name=course['name'], professor=Professor.objects.get_or_create(user=User.objects.get(username=course['professor']))[0])[0]
        t.prerequisite.set([Course.objects.get(name=pre) for pre in course['prerequisites']])
        t.time_period.set([TimePeriod.objects.get(day=day, time=time) for day, time in course['time_period']])
        t.save()

    populate_assignment()


def populate_assignment():
    pass


def populate():
    populate_time_period()
    populate_user()


if __name__ == '__main__':
    print('Starting MoodlePlus population script...')
    populate()
