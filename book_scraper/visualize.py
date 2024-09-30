import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.books_db
collection = db.books_collection

# Load data into a DataFrame
data = pd.DataFrame(list(collection.find()))

# Example: Visualize the distribution of book prices
plt.figure(figsize=(10, 6))
plt.hist(data['price'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Book Prices')
plt.xlabel('Price (in £)')
plt.ylabel('Number of Books')
plt.grid(axis='y', alpha=0.75)
plt.show()