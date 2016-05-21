import MySQLdb

conn = MySQLdb.connect('localhost','root','pass','somedb')

conn.autocommit(True)
query = "select version()"

cur = conn.cursor()
cur.execute(query)
print(cur.description[0][0])
print(cur.fetchone())
cur.close()
conn.close()