from django.contrib import admin

# Register your models here.
from .models import Room, Message, Topic

# register the Room section into the Admin Dashboards:
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)