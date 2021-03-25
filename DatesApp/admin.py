from django.contrib import admin
from DatesApp.models import TasksDate

# Register your models here.

class DatesAppAdmin(admin.ModelAdmin):

    list_display = ('date', 'is_published')
    list_display_links = ('date',)
    list_per_page = 31

admin.site.register(TasksDate, DatesAppAdmin)