import mysql.connector
def get_connection():
  conn= mysql.connector.connect(
  host="localhost",
  user="root",
  password="qwerty123",
  database="ilmanlaatu")
  return conn
