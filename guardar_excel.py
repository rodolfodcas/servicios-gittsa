import pandas as pd
import openpyxl

contador = 1
firstName = []

cantidad = int(input('Cuantos valores agregaras?\n'))

for i in range(cantidad):
    names = str(input(f'Ingresa el {contador} nombre: '))
    contador += 1
firstName.append(names)

data = firstName

df = pd.DataFrame(data, columns = ['first_name'])
df.to_excel('example.xlsx', sheet_name = 'example')