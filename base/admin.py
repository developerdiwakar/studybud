from django.contrib import admin

# Register your models here.
from .models import Room

# register the Room section into the Admin Dashboards:
admin.site.register(Room)