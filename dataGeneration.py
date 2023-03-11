import pandas as pd
import numpy as np

# Define the columns of the table
columns = ['Machine', 'Model', 'Machine Type', 'Country', 'Del.date', 'Del.Site', 'Price', 'S/w ver']

# Generate random data for the table
machine_names = ['Machine A', 'Machine B', 'Machine C', 'Machine D', 'Machine E']
models = ['Model 1', 'Model 2', 'Model 3', 'Model 4', 'Model 5']
machine_types = ['Type A', 'Type B', 'Type C', 'Type D', 'Type E']
countries = ['India', 'USA', 'UK', 'China', 'Japan']
dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
sites = ['Site A', 'Site B', 'Site C', 'Site D', 'Site E']
prices = np.random.randint(1000, 10000, size=1000)
versions = ['1.0', '2.0', '3.0', '4.0', '5.0']

# Create a dictionary of data for the table
data = {
    'Machine': np.random.choice(machine_names, size=1000),
    'Model': np.random.choice(models, size=1000),
    'Machine Type': np.random.choice(machine_types, size=1000),
    'Country': np.random.choice(countries, size=1000),
    'Del.date': np.random.choice(dates, size=1000),
    'Del.Site': np.random.choice(sites, size=1000),
    'Price': prices,
    'S/w ver': np.random.choice(versions, size=1000)
}

# Create the table
table = pd.DataFrame(data, columns=columns)

# Print the table
print(table)


