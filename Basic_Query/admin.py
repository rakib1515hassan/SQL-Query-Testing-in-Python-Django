from django.contrib import admin
from Basic_Query.models import Student, Teacher


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 's_class', 'roll', 'age', 'city', 'date_of_birth')
    ordering = ['roll']
    search_fields = ["name", "s_class", "roll"]



@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'emplyee_id', 'city', 'salary', 'joiningDate')
    ordering = ['-emplyee_id']
    search_fields = ["name", "emplyee_id", "joiningDate"]
