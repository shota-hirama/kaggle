import psycopg2
import pandas

def get_db_info(ini, header_name):
	try:
		host = ini.get(header_name, "host")
		port = ini.get(header_name, "port")
		dbname = ini.get(header_name, "dbname")
		user = ini.get(header_name, "user")
		password = ini.get(header_name, "password")
	
		return host, port, dbname, user, password

	except:
		# TODO
		return None

class use_db():
	def __init__(self, ):
		return

	def connect(self, header_name):
		host, port, dbname, user, password = get_db_info(ini, header_name)
		self.con = psycopg2.connect("host=" + host + " port=" + port + " dbname=" + dbname + " user=" + user + " password=" + password)

	def run_select(self, sql, headr):
		cur = self.con.cursor()
		cur.excute(sql)
		result = cur.fetchall()
		cur.close()