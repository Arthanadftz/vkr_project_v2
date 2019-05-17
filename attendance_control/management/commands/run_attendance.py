from django.core.management.base import BaseCommand
from django.utils import timezone

from attendance_control.models import Attendance
from users.models import CustomUser

import time
#import os
from datetime import datetime, date



class Command(BaseCommand):
    help = "Run attendance control loop"
    # Main Loop
    def generate_attendance(self):
        # Device that collect data from student's cards and save at some server
        ENDPOINT_URL = 'https://some_device.com/api_v1/get_data'

        while True:
            data = self.request(ENDPOINT_URL).json()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Data recieved at {time.time()}."
                )
            )

            with open(f'../media/documents/attendance/{time.time()}.json', 'w') as f:
                json.load(data, f, indent=4, ensure_ascii=False)

                attendance_instance = Attendance.objects.create(
                    title = f'Лист посещаемости от {date.today()}',
                    document=f,
                    date=datetime.now(),
                    author=CustomUser.get(pk=0)
                )

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Data saved at {time.time()}.\nLocation: {attendance_instance.document.url}.\nSleeping untill next call..."
                    )
                )

                time.sleep(43200)


    def handle(self, *args, **kwargs):

        self.stdout.write(
            self.style.SUCCESS(
                "Attendance control loop is starting..."
            )
        )

        self.generate_attendance()
