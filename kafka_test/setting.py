import os
import sqlite3

db_filename = 'test.db'

conn = sqlite3.connect(db_filename)
c = conn.cursor()
sql = '''create table t1 (id integer , x integer , y integer， weight real)'''

c.execute(sql)
conn.commit()


