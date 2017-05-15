import redis
from config import config
REDIS_CLI = redis.StrictRedis(host=config.get('REDIS','host'), port=config.get('REDIS','port'), db=0)