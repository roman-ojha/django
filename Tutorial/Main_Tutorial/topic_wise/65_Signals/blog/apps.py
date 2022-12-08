from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    # now after we create the signal we have to import that signal here
    def ready(self):
        import blog.signals
