from django.contrib import admin

# From the current location, import the models.py
from . import models
# Register your models with DjangoAdmin below here.

admin.site.register(models.UserProfile)
