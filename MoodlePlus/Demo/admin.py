from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TimePeriod)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Assignment)
