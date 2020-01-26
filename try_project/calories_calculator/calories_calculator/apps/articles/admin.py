from django.contrib import admin

from .models import Meal, UserProfile, create_profile

admin.site.register(Meal)
admin.site.register(UserProfile)

