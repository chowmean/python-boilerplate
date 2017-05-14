from config import config
import beanstalkc
beanstalk = beanstalkc.Connection(host=config.get('QUEUE','host'), 
								  port=config.get('QUEUE','port'))