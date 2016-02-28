import pg8000

conn = pg8000.connect(database='feverfinder')
cursor = conn.cursor()
cursor.execute("CREATE TABLE temperatures (id serial, temperature decimal, time bigint)")
conn.commit()