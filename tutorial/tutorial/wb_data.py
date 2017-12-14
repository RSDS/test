import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='wb')

cursor = conn.cursor()

cursor.execute('create table user(id VARCHAR(20) PRIMARY KEY , name VARCHAR(30))')
cursor.execute('insert into user(id, name) VALUES (%s, %s)', ['22','菊花'])
conn.commit()
cursor.close()