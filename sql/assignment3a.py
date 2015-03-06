# Assignment 3a - insert random data


# import the sqlite library
import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # delete the database table if exist
    c.execute("DROP TABLE if exists numbers")

    # create database table
    c.execute("CREATE TABLE numbers (num int)")

    # insert each number to the database
    for i in range(100):
        c.execute("INSERT INTO numbers values(?)", (random.randint(0,100),))