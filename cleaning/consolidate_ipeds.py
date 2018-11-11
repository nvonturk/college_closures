import numpy as np 
import pandas as pd 
import os

# Name directory or directories of source files

financial = "../raw/financial/"

# Concatenate IPEDS financial data

financial_files = [f for f in os.listdir(financial) if f.startswith("CSV")]
df = pd.concat([pd.read_csv(financial+file, index_col=['unitid', 'year', 'institution name']) for file in financial_files], sort=False)
df.to_csv(financial + "raw_financial.csv")

# Rename columns to remove date and institution type metadata

column_keys = {}
for value in df.columns.values:
	original_value = value
	if "." in value:
		split = value.split(".")
		value = split[1]
	if "(" in value:
		split = value.split("(")
		value = split[0]
	value = value.replace("  ", " ")
	value = value.strip()
	column_keys[original_value] = value

df = df.rename(columns=column_keys)
df = df.drop(['Status of institution', 'Date institution closed'], axis=1)
df = df.groupby(df.columns, axis=1).sum(min_count=1)

df.to_csv(financial + "raw_financial_cleaned.csv")
