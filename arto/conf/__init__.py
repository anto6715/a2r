from arto.conf import global_settings

TO_LOAD = [global_settings]


class Settings:
    def __init__(self, *modules):
        for module in modules:
            for setting in dir(module):
                if setting.isupper():
                    setattr(self, setting, getattr(module, setting))


settings = Settings(*TO_LOAD)
