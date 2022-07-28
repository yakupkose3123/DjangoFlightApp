from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    #!For user create Token
    #App çalıştığında benim yazdığım signal ı kullan demek
    def ready(self):
        import users.signals
