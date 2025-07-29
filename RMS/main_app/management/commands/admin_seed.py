from django.core.management.base import BaseCommand
from main_app.models import Role, UserInformation  # replace 'core' with your app name
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = "Seed the database with an Admin user"

    def handle(self, *args, **kwargs):
        # Ensure the 'Admin' role exists
        admin_role, _ = Role.objects.get_or_create(name="Admin")

        # Create admin user if not exists
        user, created = UserInformation.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@example.com",
                "phone": 9999999999,
                "role": admin_role,
                "password": make_password("admin@123"),
                "otp": "000000",
                "is_verified": True,
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS("✅ Admin user created successfully."))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Admin user already exists."))
