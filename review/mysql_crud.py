import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost:3606',
    user='root',
    password='',
    database='test'
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
'''
cursor.execute(create_table_query)

# Insert data
insert_query = '''
INSERT INTO users (name, age)
VALUES (%s, %s)
'''
data = ('Alice', 30)
cursor.execute(insert_query, data)

# Commit the transaction
conn.commit()

# Read data
select_query = '''
SELECT * FROM users
'''
cursor.execute(select_query)
for row in cursor.fetchall():
    print(row)

# Update data
update_query = '''
UPDATE users
SET age = %s
WHERE name = %s
'''
data = (35, 'Alice')
cursor.execute(update_query, data)
conn.commit()

# Delete data
delete_query = '''
DELETE FROM users
WHERE name = %s
'''
data = ('Alice',)
cursor.execute(delete_query, data)
conn.commit()

# Close cursor and connection
cursor.close()
conn.close()
