from os import environ as environment

from django.contrib.sites.models import Site
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        site = Site.objects.all()[0]
        site.domain = environment['DJANGO_SITE_DOMAIN']
        site.name = environment['DJANGO_SITE_NAME']
        site.save()
