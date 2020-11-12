from django.contrib import admin

from .models import Organization, Task, Profile


class OrganizationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['organization_text']}),
        ('Description', {'fields': ['description_text']}),
    ]
    list_display = ('organization_text', 'description_text')
    list_filter = ['organization_text']
    search_fields = ['organization_text']


admin.site.register(Organization, OrganizationAdmin)


class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['task_text']}),
        ('Description', {'fields': ['description_text']}),
        ('is_done', {'fields': ['is_done']}),
    ]
    list_display = ('task_text', 'description_text')
    list_filter = ['task_text']
    search_fields = ['task_text']


admin.site.register(Task, TaskAdmin)


admin.site.register(Profile)
