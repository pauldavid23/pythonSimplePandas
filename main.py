import pandas as pd

# 1. Use a dictionary with lists for each column
data = {
    'Name': ['Paul', 'Alice', 'James'],
    'Age': [30, 28, 29],
    'Location': ['US', 'Philippines', 'India']
}

# 2. Use pd.DataFrame() with a capital 'F' and pass data inside
df = pd.DataFrame(data)

# 3. Print the resulting DataFrame
print(df)
