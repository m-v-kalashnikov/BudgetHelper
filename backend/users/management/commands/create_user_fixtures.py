from core.fixtures.factories import UserFactory
from django.core.management import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--runs',
            default=1,
            type=int,
            help='Specifies the number of runs fo creation user. Default is "1".',
        )

    def handle(self, *args, **options):

        for _ in range(options['runs']):
            UserFactory()
