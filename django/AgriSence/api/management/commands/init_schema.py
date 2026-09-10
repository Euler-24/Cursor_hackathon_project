from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "Crée les tables AgriSence dans MySQL (Railway ou local)."

    def handle(self, *args, **options):
        schema = settings.BASE_DIR / "schema_mysql.sql"
        sql = schema.read_text(encoding="utf-8")
        statements = [s.strip() for s in sql.split(";") if s.strip()]
        with connection.cursor() as cursor:
            for statement in statements:
                cursor.execute(statement)
        self.stdout.write(self.style.SUCCESS("Tables AgriSence prêtes."))
