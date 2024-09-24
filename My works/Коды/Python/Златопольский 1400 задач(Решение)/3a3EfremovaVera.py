import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
url = 'https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction/download'
data = pd.read_csv(url)

# Display the first few rows of the dataset to understand its structure
data.head()

# Extract relevant columns: Price, Area, Rooms
price = data['price']
area = data['area']
rooms = data['rooms']

# Create a scatter plot
plt.figure(figsize=(12, 8))
scatter = plt.scatter(area, rooms, c=price, cmap='viridis', alpha=0.6)
plt.colorbar(scatter, label='Price')
plt.title('Real Estate Prices')
plt.xlabel('Area (sq ft)')
plt.ylabel('Number of Rooms')
plt.grid(True)
plt.show()
