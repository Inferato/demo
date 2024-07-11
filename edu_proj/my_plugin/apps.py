from django.apps import AppConfig

class MyPluginConfig(AppConfig):
    name = 'my_plugin'

    def ready():
        # Ваш код, який буде виконуватися при завантаженні додатку
        # Додайте ваш пакет до INSTALLED_APPS
        from django.conf import settings
        settings.INSTALLED_APPS.append('my_plugin')
        from my_plugin.settings import configure_settings
        configure_settings()

    #     # from django.apps import apps
    #     # apps.get_app_config('my_plugin').add_to_installed_apps()
    #     from django.conf import settings
    #     settings.INSTALLED_APPS.append('my_plugin')
    #     from my_plugin import urls
