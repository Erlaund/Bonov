from django.contrib import admin
from django import forms

# Register your models here.

from .models import *

#class MailAdmin(admin.ModelAdmin):
class MailAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('id', 'title', 'email', 'created_at', 'name', 'allow_data_process')
	list_display_links = ('title',)
	readonly_fields = ('created_at', )



admin.site.register(Mail, MailAdmin)
admin.site.site_title = 'Управление письмами'
admin.site.site_header = 'Управление письмами'

