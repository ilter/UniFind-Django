from django.contrib import admin

# Register your models here.

from .models import User, University, Agent

admin.site.register(User)
admin.site.register(University)
admin.site.register(Agent)
