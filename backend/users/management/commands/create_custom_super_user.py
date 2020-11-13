from os import environ as environment

from django.core.management import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        CustomUser.objects.create_superuser(username=environment['DJANGO_CUSTOM_SUPERUSER_USERNAME'],
                                            email=environment['DJANGO_CUSTOM_SUPERUSER_EMAIL'],
                                            password=environment['DJANGO_CUSTOM_SUPERUSER_PASSWORD'],
                                            first_name=environment['DJANGO_CUSTOM_SUPERUSER_FIRSTNAME'],
                                            last_name=environment['DJANGO_CUSTOM_SUPERUSER_LASTNAME'],
                                            )
