import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor(  )

    sql = {
            'Focus count': "SELECT count(make) FROM orders where model = 'Focus'",
            'Model T count': "SELECT count(make) FROM orders where model = 'Model T'",
            'Fiesta count': "SELECT count(make) FROM orders where model = 'Fiesta'",
            'Accord count': "SELECT count(make) FROM orders where model = 'Accord'",
            'Civic count': "SELECT count(make) FROM orders where model = 'Civic'"
            }

    for keys, values in sql.iteritems():
        c.execute(values)

        result = c.fetchone()

        print keys + ":", result[0]