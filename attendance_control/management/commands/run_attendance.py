from django.core.management.base import BaseCommand
from django.core.files import File
from django.utils import timezone

from attendance_control.models import Attendance
from users.models import CustomUser

import os
import pandas as pd
import requests
import time

from datetime import datetime, date


class Command(BaseCommand):
    help = "Run attendance control loop"
    # Main Loop
    def generate_attendance(self):
        # Device that collect data from student's cards and save at some server
        ENDPOINT_URL = 'https://some_device.com/api_v1/get_data'

        while True:
            data = requests.get(ENDPOINT_URL).json()
            fname = f'Журнал-{data.get('disciple')}-{data.get('date')}_a.csv'
            fdir = 'attendance_control/atts_csv/{fn}'

            self.stdout.write(
                self.style.SUCCESS(
                    f"Data recieved at {time.time()}."
                )
            )

            attendance_instance = Attendance.objects.create(
                group=data.get('group'),
                disciple=data.get('disciple'),
                date=data.get('date'),
                author=CustomUser.get(pk=0)
            )

            df = pd.DataFrame(
                {
                    "ФИО студента": data.get("students_list"),
                    "Присутствие": data.get("check_list")
                    }
                )

            df.to_csv(fdir.format(fn=fname))

            with open(fdir.format(fn=fname)) as f:
                my_file = File(f)
                attendance_instance.document.save(fname, my_file)

            os.system(f"cd {fdir[:-4]} && rm *.csv")

            self.stdout.write(
                self.style.SUCCESS(
                    f"Data saved at {time.time()}.\nLocation: {attendance_instance.document.url}. Tmp files removed.\nSleeping untill next call..."
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
