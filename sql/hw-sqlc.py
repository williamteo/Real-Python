import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("UPDATE inventory SET Quantity = 60 WHERE Model = 'Model T'")

	c.execute("UPDATE inventory SET Quantity = 100 WHERE Model = 'Focus'")
	
	c.execute("SELECT * FROM inventory")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]
