from django.apps import AppConfig

class GameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'game'

    def ready(self):
        import game.signals  # Importa las señales al cargar la aplicación
