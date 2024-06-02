# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Create a list of grades
grades = [60, 70, 80, 90, 100, 80, 70, 60, 50, 40]

# Calculate the mean and standard deviation of the grades
mean = np.mean(grades)
std = np.std(grades)

# Create a range of grades
x = np.arange(len(grades))
y=[grades[i]+std for i in range(len(x))]

# Create a line chart of the grades with the standard deviation values displayed
plt.plot(x, grades, 'o')
plt.plot(x, y, 'ro')
# plt.plot(x, mean - std, 'r--')
plt.title('Grades and Standard Deviation')
plt.xlabel('Student')
plt.ylabel('Grade')
plt.show()

# Generate a random sample from a normal distribution with mean 0 and standard deviation 1
sample = np.random.normal(0, 1, 1000)

# Create a DataFrame with the sample
df = pd.DataFrame(sample, columns=['Sample'])

# Plot a histogram of the sample
df.hist(bins=50)

# Show the plot
plt.show()
# %%
