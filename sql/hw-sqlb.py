import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	cars = [
				('Ford','Focus', 27),
				('Ford','Fiesta', 74),
				('Ford','Model T', 35),
				('Honda','Accord', 62),
				('Honda','Civic', 10)
	]

	c.executemany("INSERT INTO inventory(Make, Model, Quantity) values (?, ?, ?)", cars)