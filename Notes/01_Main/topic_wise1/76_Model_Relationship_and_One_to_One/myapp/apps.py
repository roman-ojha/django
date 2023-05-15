from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    # using signal that we created on './signals.py'

    def ready(self):
        import myapp.signals
