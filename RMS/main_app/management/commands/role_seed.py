from django.core.management.base import BaseCommand
from main_app.models import Role  

class Command(BaseCommand):
    help = "Seed the database with default roles"

    def handle(self, *args, **kwargs):
        roles = ["admin", "recruiter", "candidate"]

        for role_name in roles:
            role, created = Role.objects.get_or_create(name=role_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created role: {role_name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Role already exists: {role_name}"))
