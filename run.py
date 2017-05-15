from config import config
from mysqlconn import conn
from logger import logger, sentry
from bstalk import beanstalk
from redisconn import REDIS_CLI
if conn:
	print "Connection Succesfull"

print logger
print sentry
print beanstalk
print REDIS_CLI

print "testing travis"