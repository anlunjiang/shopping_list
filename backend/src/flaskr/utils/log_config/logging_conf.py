import logging.config
import os

logging.config.fileConfig(
    os.path.join(os.path.dirname(__file__), "logging.ini"),
    disable_existing_loggers=False,
)

logger = logging.getLogger("shop_backend_flask")
