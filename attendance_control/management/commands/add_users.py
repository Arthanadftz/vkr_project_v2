from django.core.management.base import BaseCommand
from django.utils import timezone

from users.models import CustomUser

import hashlib
import random

from datetime import datetime, date


def add_users():
    names = ['Сидоров Сергей Иванович', 'Петров Олег Павлович', 'Григорьев Григорий Григорьевич']
    h = hashlib.new('ripemd160')

    for i in range(5,15):
        usname = f"student{i}"
        h.update(usname.encode())
        #pwd = h.hexdigest()[:10]
        pwd = '19962204Bb'
        eml = f"{usname}@gmail.com"
        name = random.choice(names)

        CustomUser.objects.create(
            username=usname,
            password=pwd,
            email=eml,
            full_name=name,
        )



class Command(BaseCommand):
    help = "Add users"
    # Main Loop
    def handle(self, *args, **kwargs):

        self.stdout.write(
            self.style.SUCCESS(
                "Adding users..."
            )
        )

        add_users()

        self.stdout.write(
            self.style.SUCCESS(
                "Users have been added..."
            )
        )
