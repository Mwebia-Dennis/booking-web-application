#import your connector
#import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="booking_database"
)
