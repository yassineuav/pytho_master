import pymongo

# Replace with your MongoDB Atlas connection URI
uri = "<your_connection_uri>"

client = pymongo.MongoClient(uri)

# Select the database and collection
db = client["mydatabase"]
collection = db["mycollection"]

# Create
data_to_insert = {"name": "John Doe", "age": 30}
inserted_data = collection.insert_one(data_to_insert)
print("Document inserted with ID:", inserted_data.inserted_id)

# Read
result = collection.find_one({"name": "John Doe"})
print("Read document:", result)

# Update
update_query = {"name": "John Doe"}
new_values = {"$set": {"age": 31}}
collection.update_one(update_query, new_values)
print("Document updated.")

# Read after update
result_after_update = collection.find_one({"name": "John Doe"})
print("Read document after update:", result_after_update)

# Delete
delete_query = {"name": "John Doe"}
collection.delete_one(delete_query)
print("Document deleted.")

# Close the connection
client.close()
