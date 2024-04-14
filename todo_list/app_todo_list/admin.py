from django.contrib import admin

from .models import Tag, Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("description", "deadline", "is_done")
    list_editable = ("is_done",)


admin.site.register(Tag)
admin.site.register(Task, TaskAdmin)
