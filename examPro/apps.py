from django.apps import AppConfig


class ExamproConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'examPro'

    def ready(self):
        import examPro.signals
