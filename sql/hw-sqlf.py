import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT inventory.make, inventory.model, inventory.quantity,
    orders.order_date FROM inventory INNER JOIN orders ON inventory.model =
    orders.model""")

    rows = c.fetchall()

    for r in rows:
        print "Make: " + r[0] + " Model: " + r[1]
        print "Quantity: " + str(r[2])
        print "Order Dates: " + r[3]
        print