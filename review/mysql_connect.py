
import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# CREATE (Insert) operation
def create_record():
    sql = "INSERT INTO employees (first_name, last_name) VALUES (%s, %s)"
    values = ("John", "Doe")
    cursor.execute(sql, values)
    conn.commit()
    print("Record inserted successfully.")

# READ (Select) operation
def read_records():
    sql = "SELECT * FROM employees"
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
        print(record)

# UPDATE operation
def update_record():
    sql = "UPDATE employees SET last_name = %s WHERE first_name = %s"
    new_last_name = "Smith"
    first_name = "John"
    cursor.execute(sql, (new_last_name, first_name))
    conn.commit()
    print("Record updated successfully.")

# DELETE operation
def delete_record():
    sql = "DELETE FROM employees WHERE first_name = %s"
    first_name = "John"
    cursor.execute(sql, (first_name,))
    conn.commit()
    print("Record deleted successfully.")

# Example usage:
create_record()
read_records()
update_record()
delete_record()

# Close the cursor and connection
cursor.close()
conn.close()
