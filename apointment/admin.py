
# Register your models here.
from atexit import register
from django.contrib import admin
from .models import *
 
 
"""
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'image', 'description')
admin.site.register(Catagory,CategoryAdmin)
"""
 
admin.site.register(drCategory)
admin.site.register(docter)
admin.site.register(Appointmentorder))
 