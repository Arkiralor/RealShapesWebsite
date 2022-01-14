from django.apps import AppConfig
from django.db.models import BigAutoField


class RstoreConfig(AppConfig):
    name = 'rstore'
    default_auto_field = 'django.db.models.BigAutoField'
