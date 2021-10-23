import xlrd
import pandas as pd
from openpyxl import load_workbook

archivo = 'C:/Users/Becario Servicios/Desktop/PY/example.xlsx'

df = pd.read_excel(archivo, sheet_name='example')

print(df)

'''archivo = 'C:/Users/Becario Servicios/Desktop/PY/example.xlsx'
  
wb = xlrd.open_workbook(archivo) 

hoja = wb.sheet_by_index(0) 
print(hoja.nrows) 
print(hoja.ncols) 
print(hoja.cell_value(0, 0))'''

'''wb = load_workbook(filename='example.xlsx', read_only=True)
ws = wb['FILTRO 1ER PARTE']

for row in ws.rows:
    for cell in row:
        print(cell.value)

# Close the workbook after reading
wb.close()'''