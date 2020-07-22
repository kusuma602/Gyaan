from django.apps import AppConfig


class GyaanAuthAppConfig(AppConfig):
    name = "gyaan_auth"

    def ready(self):
        from gyaan_auth import signals # pylint: disable=unused-variable
