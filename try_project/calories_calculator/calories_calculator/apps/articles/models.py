from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings


class Meal(models.Model):
    class Meta:
        app_label = 'meals'
        ordering = ('date', 'time')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    calories = models.IntegerField()

    def __str__(self):
        return self.description


class UserProfile(models.Model):
    class Meta:
        app_label = 'meals'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    expected_daily_calories = models.IntegerField()


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        up = UserProfile(
            user=user,
            expected_daily_calories=settings.DEFAULT_DAILY_CALORIES)
        up.save()


post_save.connect(create_profile, sender=User)
