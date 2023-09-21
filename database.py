import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    port=8889,
    database="testdb"
)

# Create cursor instance
my_cursor = mydb.cursor()

# Create a Database
my_cursor.execute("CREATE DATABASE testdb")

# Show Databases
my_cursor.execute("SHOW DATABASES")

# Create a table
my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
my_cursor.execute("SHOW TABLES")

# Insert 1 record
user = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("John", "john@gmail.com", 35)
my_cursor.execute(user, record1)
mydb.commit()

# Insert Multiple Records
user = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
records = [
  ("Tim", "tim@gmail.com", 26),
  ("Jane", "jane@gmail,com", 20),
  ("Mike", "mike@gmail.com", 38),
  ("Chris", "chris@gmail.com", 44)
]
my_cursor.executemany(user, records)
mydb.commit()

# Retrieve data from table
my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()
for i in result:
    print(i)

# Where Clause
my_cursor.execute("SELECT * FROM users WHERE age < 30")
result = my_cursor.fetchall()
for i in result:
    print(i)

# Where Like and Wildcards
my_cursor.execute("SELECT * FROM users WHERE name LIKE 'J%'")
result = my_cursor.fetchall()
for i in result:
    print(i)

# AND / OR Clause
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%o%' AND age > 20 OR age = 35")
result = my_cursor.fetchall()
for i in result:
    print(i)

# Updating Records
my_sql = "UPDATE users SET age = 33 WHERE user_id = 16"
my_cursor.execute(my_sql)
mydb.commit()

# Limit Results
my_cursor.execute("SELECT * FROM users LIMIT 3 OFFSET 1")
result = my_cursor.fetchall()
for i in result:
    print(i)

# Delete Records
my_sql = "DELETE FROM users WHERE user_id = 5"
my_cursor.execute(my_sql)
mydb.commit()

# Delete table
my_sql = "DROP TABLE users"
my_cursor.execute(my_sql)
