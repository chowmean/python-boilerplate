import logging
import graypy
from config import config

logger = logging.getLogger(config.get('LOGGER','name'))
logger.setLevel(logging.DEBUG)

handler = graypy.GELFHandler(config.get('LOGGER','host'),
							 config.get('LOGGER','port'))
logger.addHandler(handler)
