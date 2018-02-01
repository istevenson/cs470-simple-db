## Imon Stevenson
## 14192284
## Assignment #1 in Python
## February 3, 2018

import sqlite3

def create_table(dbname, tablename, statement):
    with sqlite3.connect(dbname) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?", (tablename,))
        response = cursor.fetchall()
        recreate_table = False
        if len(response) == 1:
            user_message = raw_input("The {0} table exists already, do you want to recreate it? (y/n): ".format(tablename))
            if user_message == "y":
                recreate_table = True
                print("Ok, recreating {} table...")
                cursor.execute("drop table if exists {0}".format(tablename))
                db.commit()
            else:
                print("Ok, {0} table kept.")
        else:
            recreate_table = True
        if not recreate_table:
            cursor.execute(statement)
            db.commit()


if __name__ == "__main__":
    dbname = "car_dealership.db"
    statement = """create table Car
             (CarID integer,
             Make text,
             Model text,
             Color text,
             Year integer,
             Price real,
             Condition text,
             primary key(CarID))"""
    create_table(dbname, "Car", statement)

def insert_item(values):
    with sqlite3.connect(dbname) as db:
        cursor = db.cursor()
        statement = """insert into Car (Make, Model, Color,
                       Year, Price, Condition) values
                       (?, ?, ?, ?, ?, ?)"""
        cursor.execute(statement, values)
        db.commit()

if __name__ == "__main__":
    values = ("Ford", "Explorer", "White",
             2012, 10000, "Used")
    insert_item(values)
             
