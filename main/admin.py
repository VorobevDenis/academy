from django.contrib import admin

from main.models import Department, Employee


@admin.register(Department)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id_department', 'name_department']
    search_fields = ['name_department']


@admin.register(Employee)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id_employee', 'name', 'post', 'salary', 'age', 'id_department']
    list_filter = ('id_department__name_department', )
    search_fields = ['name', 'post', 'age', 'salary', 'id_department__name_department']

