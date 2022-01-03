from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

    # Sobrepose method for init updater when initializate the project
    def ready(self):
        from posts import updater
        updater.start()
