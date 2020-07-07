from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError
from user_activities.models import User, ActivityPeriod
import pytz
import random


class Command(BaseCommand):
    help = 'Generates random dummy data of users and activity logs'
    def handle(self, *args, **kwargs):
        users = [
            User(
                real_name='Test User' + str(i),
                timezone='Asia/Kolkata'
            )
            for i in range(1, 5)
        ]

        User.objects.bulk_create(users)

        tz = pytz.timezone('Asia/Kolkata')
        for user in User.objects.all():
            activities = [
                ActivityPeriod(
                    user=user,
                    start_time=datetime.now(tz)-timedelta(
                        days=i, minutes=random.randint(50, 200)
                    ),
                    end_time=datetime.now(tz)-timedelta(days=i)
                )
                for i in range(1, 5)
            ]

            ActivityPeriod.objects.bulk_create(activities)



        self.stdout.write(self.style.SUCCESS('Data generated successfully'))
