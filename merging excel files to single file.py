#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pathlib import Path

# Specify the directory containing the Excel files
directory = Path('/Users/gangasingh/Downloads/Cricket')

# Initialize an empty list to store DataFrames
dfs = []

# Loop through each file in the directory
for filename in directory.glob('*.xlsx'):
    # Read the Excel file into a DataFrame and append it to the list
    dfs.append(pd.read_excel(filename))

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged DataFrame to a new Excel file
output_file = directory / 'Final.xlsx'
merged_df.to_excel(output_file, index=False)

print(f"Merged DataFrame saved to {output_file}")

