from django.contrib import admin

# Register your models here.

from .models import student
from .models import Datas

admin.site.register(student)
admin.site.register(Datas)
