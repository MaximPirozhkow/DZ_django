from django.contrib import admin
from .models import BugReport, FeatureRequest



@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')

# Register your models here.

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project', 'task')
    search_fields = ('title', 'description')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')