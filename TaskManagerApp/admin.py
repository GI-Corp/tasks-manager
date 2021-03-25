from django.contrib import admin
from TaskManagerApp.models import Tasks
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class TasksAdmin(ImportExportModelAdmin):

    list_display = ('id', 'date', 'category', 'sign', 'contract_id_unique', 'task_date', 'content', 'responsible_user', 'task_deadline', 'result', 'verification')
    list_display_links = ('date',)
    list_filter = ('category', 'responsible_user',)
    # Search by these attributes || For foreign keys add __name to avoid error
    search_fields = ('sign', 'contract_id_unique', 'task_date', 'content', 'task_deadline', 'result', 'verification',)
    list_per_page = 30


admin.site.register(Tasks, TasksAdmin)
# @admin.register(Tasks)
# class ViewAdmin(ImportExportActionModelAdmin):
#     pass