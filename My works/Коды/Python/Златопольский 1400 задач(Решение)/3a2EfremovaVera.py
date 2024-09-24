# Generate 2000 random numbers with normal distribution
mean = 5   # Arbitrary mean
std_dev = 2  # Arbitrary standard deviation
data = np.random.normal(mean, std_dev, 2000)

# Plot the normalized histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=50, density=True, alpha=0.6, color='b')

# Plot the normal distribution curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = np.exp(-0.5 * ((x - mean) / std_dev)**2) / (std_dev * np.sqrt(2 * np.pi))
plt.plot(x, p, 'k', linewidth=2)

# Add title and labels
plt.title('Normalized Histogram of 2000 Random Numbers with Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(True)
plt.show()
