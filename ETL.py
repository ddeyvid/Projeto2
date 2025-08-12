import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    #password='',
    database='olist'
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS""")