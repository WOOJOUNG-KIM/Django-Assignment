from django.contrib import admin
from todo.models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'start_date', 'end_date')
    list_filter = ('is_completed',)
    search_fields = ('title',)
    ordering = ('start_date',)
    fieldsets = (
        ('Todo 정보', {
            'fields': ('title', 'description', 'is_completed')
        }),
        ('기간 설정', {
            'fields': ('start_date', 'end_date')
        }),
    )
