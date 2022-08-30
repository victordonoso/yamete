from django.contrib import admin

# Register your models here.

from .models import Events, Matches

admin.site.register(Events)
admin.site.register(Matches)