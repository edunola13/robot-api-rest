from django.apps import AppConfig


class ManufactersConfig(AppConfig):
    name = 'manufacters'

   	def ready(self):
        import apps.manufacters.signals