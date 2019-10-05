''' Concatenate all the csv files into 1 '''

import pandas as pd

# Load the three datasets
DATA1 = pd.read_csv("Accumulated_csv_for_each_page/Computer_Professors20.csv")
DATA2 = pd.read_csv("Accumulated_csv_for_each_page/Computer_Professors24.csv")
DATA3 = pd.read_csv("Accumulated_csv_for_each_page/Computer_Professors25.csv")

# Drop the rows that were repeated
DATA1 = DATA1.iloc[0:190, :]

# Concatenate the datasets into 1
DATA = pd.concat([DATA1, DATA2]).reset_index(drop=True)
DATA = pd.concat([DATA, DATA3]).reset_index(drop=True)

# Convert to csv
DATA.to_csv('Computer_Professors.csv', index=False)
