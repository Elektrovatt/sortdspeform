from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'
    verbose_name = 'Аккаунт'

class ProfilesConfig(AppConfig):
    name = 'profiles'
    verbose_name = 'Профиль аккаунта'


