# Dependencies
import pandas as pd

# Store filepath in a variable
file_one = "Resources/cities.csv"

# Read our Data file with the pandas library
# Not every CSV requires an encoding, but be aware this can come up
file_one_df = pd.read_csv(file_one)

file_one_html = file_one_df.to_html("Resources/cities.html", index=False, header=True)
