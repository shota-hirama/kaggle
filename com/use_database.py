import psycopg2
import pandas

def set_db_info(ini, header_name):
	try:
		host = ini.get(header_name, "host")
		port = ini.get(header_name, "port")
		dbname = ini.get(header_name, "dbname")
		user = ini.get(header_name, "user")
		password = ini.get(header_name, "password")
	
		return host, port, dbname, user, password