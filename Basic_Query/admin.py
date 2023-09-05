from django.contrib import admin
from Basic_Query.models import Student, Teacher


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 's_class', 'roll', 'age', 'city', 'date_of_birth')





# admin.site.register(Student)