import logging
import graypy
from config import config
from raven import Client

logger = logging.getLogger(config.get('LOGGER','name'))
logger.setLevel(logging.DEBUG)
handler = graypy.GELFHandler(config.get('LOGGER','host'),
							 config.get('LOGGER','port'))
logger.addHandler(handler)

sentry = Client(config.get('SENTRY','uri'))
