import mysql.connector
# create_database.py
db_conn = mysql.connector.connect(host="localhost", user="ram", password="Password", database="arch")
db_cursor = db_conn.cursor()

db_cursor.execute('''
DROP TABLE media_playbacks, media_uploads
''')
db_conn.commit()
db_conn.close()
print('done')