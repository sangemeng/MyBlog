from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'subject', 'content', 'id']
