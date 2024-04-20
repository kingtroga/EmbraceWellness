from django.contrib import admin

from .models import Forum 


class ForumAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at', 'modified_at']

admin.site.register(Forum, ForumAdmin)