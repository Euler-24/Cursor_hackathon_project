from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from django.conf import settings

        if getattr(settings, 'TESTING', False):
            for model in self.get_models():
                model._meta.managed = True
