import mysql.connector as mariadb, sys, os
from dotenv import load_dotenv

mariadb_connection = None

def fetch_assoc(cursor):
	return dict(zip(cursor.column_names, cursor.fetchone()))

def getdb():
	global mariadb_connection
	
	if not mariadb_connection:
		
		load_dotenv()
		db_user = os.getenv('DB_USER')
		db_pass = os.getenv('DB_PASS')
		db_host = os.getenv('DB_HOST')
		db_port = os.getenv('DB_PORT')
		db_name = os.getenv('DB_DATABASE')

		try:
			connection = mariadb.connect(user='testrootuser', password='mdb_pass_goodbad!', host='192.168.1.157', port='3306', database = 'LilBuddy')

		except mariadb.Error as e:
			print(f"Error connecting to MariaDB Platform: {e}")
			sys.exit(1)
			
		mariadb_connection = connection

	return mariadb_connection