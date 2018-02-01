## Imon Stevenson
## DB in Python
## February 3, 2018

import sqlite3

## check if table exists, create new if not
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
                print("Ok, recreating {} table...").format(tablename))
                cursor.execute("drop table if exists {0}".format(tablename))
                db.commit()
            else:
                print("Ok, {0} table kept.")
        else:
            recreate_table = True
        if recreate_table:
            cursor.execute(statement)
            db.commit()


## create tables
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

if __name__ == "__main__":
    dbname = "car_dealership.db"
    statement = """create table Customer
                (CustomerID integer,
                FullName text,
                Email text,
                Phone text,
                DOB text,
                primary key(CustomerID))"""
    create_table(dbname, "Customer", statement)


## insert new items to tables
def insert_item(tablename, values):
    with sqlite3.connect(dbname) as db:
        cursor = db.cursor()
        if tablename == "Car":
            statement = """insert into Car (Make, Model, Color,
                           Year, Price, Condition) values
                           (?, ?, ?, ?, ?, ?)"""
        else:
            statement = """insert into Customer (FullName,
                                 Email, Phone, DOB) values
                                 (?, ?, ?, ?)"""
        cursor.executemany(statement, values)
        db.commit()

if __name__ == "__main__":
    car_values = [("Ford", "Explorer", "White",
                    2012, 10000, "Used"),
                  ("Toyota", "Highlander", "Midnight Blue",
                    2010, 12000, "Used"),
                  ("Jeep", "Grand Cherokee", "Black",
                   2006, 4999, "Used")]
    
    customer_values = [("John Smith", "jsmith@gmail.com",
                        "816-555-1234", "08-19-1985"),
                       ("Jane Doe", "jdoe@yahoo.com",
                        "913-555-4321", "03-01-1972")]
    insert_item("Car", car_values)
    insert_item("Customer", customer_values)

## update items
def update_item(tablename, values):
    with sqlite3.connect(dbname) as db:
        cursor = db.cursor()
        if tablename == "Car":
            statement = "update Car set Color=? where CarID=?"
        else:
            statement = "update Customer set FullName=? where CustomerID=?"
        cursor.execute(statement, values)
        db.commit()

if __name__ == "__main__":
    car_value = ("Silver", 1)
    customer_value = ("Jayne Doe", 2)
    update_item("Car", car_value)
    update_item("Customer", customer_value)
