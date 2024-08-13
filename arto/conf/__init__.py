from arto.conf import global_settings

TO_LOAD = [global_settings]


class Settings:
    def __init__(self, *modules):
        for module in modules:
            for setting in dir(module):
                if setting.isupper():
                    setattr(self, setting, getattr(module, setting))

    def configure(self, **ext_settings):
        """Set new settings or override default ones."""
        for key, value in ext_settings.items():
            if key.isupper():
                setattr(self, key, value)


settings = Settings(*TO_LOAD)
