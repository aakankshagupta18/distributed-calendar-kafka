import psycopg2

conn = psycopg2.connect("dbname=calendar_db user=postgres password=**** host=localhost")
cursor = conn.cursor()


cursor.execute("SELECT * FROM events;")
print(cursor.fetchall())


