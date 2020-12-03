from django.contrib import admin

# Register your models here.
from .models import Faculty
from .models import Student
from .models import Administrative

admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Administrative)

