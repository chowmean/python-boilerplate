from config import config
from mysqlconn import conn
from logger import logger, sentry
from bstalk import beanstalk
if conn:
	print "Connection Succesfull"

print logger
print sentry
print beanstalk

print "testing travis"