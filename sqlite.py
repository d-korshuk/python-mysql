import sqlite3

# Query the DB and return all records
def show_all():
    # Connect to DB and create cursor
    con = sqlite3.connect('customers.db')
    cursor = con.cursor()

    # Query the DB 
    cursor.execute("SELECT * FROM customers")
    items = cursor.fetchall()

    for i in items:
        print(i)

    # Commit the command and close connection
    con.commit()
    con.close()


# Add a new record to the table
def add_one(first, last, email):
    # Connect to DB and create cursor
    con = sqlite3.connect('customers.db')
    cursor = con.cursor()
    con.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    # Commit the command and close connection
    con.commit()
    con.close()


# Add many records to the table
def add_many(list):
    # Connect to DB and create cursor
    con = sqlite3.connect('customers.db')
    cursor = con.cursor()
    con.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    # Commit the command and close connection
    con.commit()
    con.close()


# Delete records from table
def delete_one(id):
     # Connect to DB and create cursor
    con = sqlite3.connect('customers.db')
    cursor = con.cursor()
    con.execute("DELETE FROM customers WHERE rowid = (?)", id)

    # Commit the command and close connection
    con.commit()
    con.close()



# Add one record to the DB
add_one("Laura", "Jackson", "laura@gmail.com")

# Add many records to the DB
stuff = [
    ("Brenda","Lewis","brenda@gmai.com"),
    ("Nick","Mcgregor","nick@gmail.com")
]
add_many(stuff)

# Delete record using rowid as a string
delete_one('6')

# Show all records
show_all()