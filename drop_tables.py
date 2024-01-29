import sqlite3

conn = sqlite3.connect('media_server.db')

c = conn.cursor()
c.execute('''
          DROP TABLE media_playbacks;
          ''')
c.execute('''
          DROP TABLE media_uploads;
          ''')
conn.commit()
conn.close()
