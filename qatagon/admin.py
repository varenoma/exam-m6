from django.contrib import admin
from .models import QatagonClass


@admin.register(QatagonClass)
class QatagonClassAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'died_date',
                    'region', 'ayblov', 'created_at')
    search_fields = ('full_name', 'region', 'ayblov')
