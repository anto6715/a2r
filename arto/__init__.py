from arto.conf import settings
from arto.utils.log import configure_logging


def setup():
    configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
