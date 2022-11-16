import pandas as pd
import openpyxl
import os

df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  columns=['Test ID', 'Test Name', 'jmeter versions'])

df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')
if os.path.exists("pandas_to_excel.xlsx"):
   os.remove("pandas_to_excel.xlsx")

newpath = 'excels'
if not os.path.exists(newpath):
    os.makedirs(newpath)