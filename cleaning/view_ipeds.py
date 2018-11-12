import pandas as pd 
import numpy as np 
import os
import matplotlib.pyplot as plt

# Name directory or directories of source files

financial_cleaned = "../raw/financial/raw_financial_cleaned.csv"
df = pd.read_csv(financial_cleaned)
df = df.set_index(['unitid', 'year', 'institution name'])
df.sort_values(by=['year'], inplace=True)

revenues = [r for r in df.columns.values if ("revenue" in r or "Revenue" in r)]
expenses = [e for e in df.columns.values if ("expense" in e or "Expense" in e)]

print(revenues)
print(expenses)

all_revenues = df.xs('Revenues from tuition and fees per FTE', axis=1)
all_expenses = df.xs('Instruction expenses per FTE', axis=1)

total_rev = all_revenues.groupby(level=1).sum()
total_exp = all_expenses.groupby(level=1).sum()
years = [2010 + i for i in range(8)]

print(total_rev.index)

plt.plot(total_rev.index, total_rev, 'g', total_exp.index, total_exp, 'r')
plt.show()

