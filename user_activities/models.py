from django.db import models

# Create your models here.


class User(models.Model):
    real_name = models.CharField(max_length=50)
    timezone = models.CharField(max_length=20)

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')

