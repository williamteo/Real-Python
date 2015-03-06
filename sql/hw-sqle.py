import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE orders 
                (make TEXT, model TEXT, order_date DATE)
                """)

    orders = [
            ('Ford','Focus','2014-02-14'),
            ('Ford','Focus','2015-03-12'),
            ('Ford','Focus','2012-02-17'),
            ('Ford','Fiesta','2013-02-28'),
            ('Ford','Fiesta','2010-04-13'),
            ('Ford','Fiesta','2009-04-24'),
            ('Ford','Model T','2014-02-04'),
            ('Ford','Model T','2012-06-01'),
            ('Ford','Model T','2011-11-27'),
            ('Honda','Accord','2014-03-31'),
            ('Honda','Accord','2012-12-12'),
            ('Honda','Accord','2013-02-06'),
            ('Honda','Civic','2011-07-17'),
            ('Honda','Civic','2010-05-03'),
            ('Honda','Civic','2008-03-19')
            ]

    c.executemany("INSERT INTO orders values(?, ?, ?)", orders)

    c.execute("SELECT * FROM orders ORDER BY order_date ASC")

    rows = c.fetchall()

    for r in rows:
        print r[0],r[1],r[2]