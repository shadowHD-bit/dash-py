import pandas as pd

# Get orders dataframe from XLSX table
MAIN_DF = pd.read_excel('data\data.xlsx')

# Get returns dataframe from XLSX table
RETURNS_DF = pd.read_excel('data\data.xlsx', sheet_name='Returns')
