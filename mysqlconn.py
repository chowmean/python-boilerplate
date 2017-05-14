import mysql.connector
from config import config
conn = mysql.connector.connect(host=config.get('DB','host'),
							   database=config.get('DB','db'),
							   user=config.get('DB','user'),
							   password=config.get('DB','password'))
