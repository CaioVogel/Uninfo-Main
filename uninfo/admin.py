from django.contrib import admin
from .models import Post, comment

class commentAdmin(admin.ModelAdmin):
  list_display = ['name','post','created_on']
  list_filter = ['created_on']
  search_fields = ['name','post','created_on']

admin.site.register(comment, commentAdmin)

class postAdmin(admin.ModelAdmin):
  list_display = ['name']

admin.site.register(Post, postAdmin)