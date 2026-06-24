from django.contrib import admin

from .models import Company, Bino

admin.site.register([Company, Bino])