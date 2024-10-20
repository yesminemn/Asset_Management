from django.core.management.base import BaseCommand
from assets.models import Employee, Asset

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create test employees
        employees = [
            Employee(name='Alice Johnson'),
            Employee(name='Bob Smith'),
            Employee(name='Charlie Brown'),
            Employee(name='Diana Prince')
        ]

        Employee.objects.bulk_create(employees)
        self.stdout.write(self.style.SUCCESS('Successfully created test employees.'))

        # Create test assets
        assets = [
            Asset(name='Laptop', available=True),
            Asset(name='Projector', available=True),
            Asset(name='Whiteboard', available=False),
            Asset(name='Desk', available=True)
        ]

        Asset.objects.bulk_create(assets)
        self.stdout.write(self.style.SUCCESS('Successfully created test assets.'))
