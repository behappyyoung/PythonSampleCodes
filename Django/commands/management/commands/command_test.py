from django.core.management import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        print(parser)
        parser.add_argument('myargument', type=str)
        print(parser)

    def handle(self, *args, **options):
        print(args)
        print(options)
        arguments = options['myargument'].split('/')
        if len(arguments) > 1:
            arg1 = arguments[0]
            arg2 = arguments[1]
        else:
            arg1 = arguments[0]
            arg2 = None

        print(arguments, arg1, arg2)