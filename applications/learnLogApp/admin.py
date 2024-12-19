from django.contrib import admin
from .models import LearnLog

@admin.register(LearnLog)
class LearnLogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'priority', 'progress', 'date_created', 'date_updated')