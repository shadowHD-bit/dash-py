import pandas as pd

# Получение датафрейма из XLSX таблица
MAIN_DF = pd.read_excel('data\data.xlsx')

# Получение датафрейма возвратов из XLSX таблица
RETURNS_DF = pd.read_excel('data\data.xlsx', sheet_name='Returns')