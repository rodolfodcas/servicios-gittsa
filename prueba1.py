import pandas as pd
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


def Ventana():

	#texto archivo excel
	ExcelLabel = Label(vn, text= "Archivo excel: ", bg = "steelblue", font = ('',18,'bold'))
	ExcelLabel.grid(row = 0, column = 0, padx = 5, pady = 5)

	#textfield del archivo excel
	vn.Entrada = Text(vn, height = 4, width = 45, font=('arial',10))
	vn.Entrada.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)


	#boton para cargar el archivo en excel
	BtnCargar = Button(vn, text= "Cargar", width = 20, height = 2, command = Cargar)
	BtnCargar.grid(row = 0, column = 3, padx=5, pady = 5)

	#texto VERIFICAR
	ExcelLabel = Label(vn, text= "Verificar: ", bg = "steelblue", font = ('',18,'bold'))
	ExcelLabel.grid(row = 1, column = 0, padx = 5, pady = 5)

	#Mostrar contenido
	ExcelLabel = Label(vn, text= "Contenido: ", bg = "steelblue", font = ('',18,'bold'))
	ExcelLabel.grid(row = 2, column = 0, padx = 5, pady = 5)
	
	#archivo veriifcado - url
	vn.archivoUrl = Text(vn, height = 4, width = 45, font=('arial',10))
	vn.archivoUrl.grid(row = 1, column = 1, columnspan = 2, padx = 5, pady = 5)

	#archivo veriifcado - url
	vn.archivoTabla = Text(vn, height = 20, width = 100, font=('arial',10))
	vn.archivoTabla.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 5)

	#boton para cargar el archivo en excel
	BtnCargar = Button(vn, text= "Verificar", width = 20, height = 2, command = Verifica)
	BtnCargar.grid(row = 1, column = 3, padx=5, pady = 5)

	#boton para cargar el archivo en excel
	BtnCargar = Button(vn, text= "Mostrar contenido", width = 20, height = 2, command = AbrirArchivo)
	BtnCargar.grid(row = 2, column = 3, padx=5, pady = 5)

	'''#boton para abrir el archivo en excel
	BtnCargar = Button(vn, text= "Abrir Archivo", width = 20, height = 2, command = AbrirArchivo)
	BtnCargar.grid(row = 2, column = 3, padx=5, pady = 5)
'''

def Cargar():
	vn.ArchivoLista = filedialog.askopenfilename(initialdir= "C:\\Users")
	vn.Entrada.insert("1.0", "Los siguientes archivos seran descomprimidos\n")
	vn.archivos = os.path.basename(vn.ArchivoLista)
	vn.Entrada.insert("2.0",vn.archivos+"\n")
	vn.Entrada.config(state=DISABLED)
	print(vn.ArchivoLista)

	#monstrar aviso
	messagebox.showinfo("Exito", "Archivos Cargado")


def Verifica():
	archivo = vn.ArchivoLista
	#df = pd.read_excel(archivo, sheet_name='example')
	vn.archivoUrl.insert('1.0', archivo)

def AbrirArchivo():
	archivo = vn.archivos
	df = pd.read_excel(archivo, sheet_name='example')
	vn.archivoTabla.insert('1.0', pd)

vn = tk.Tk()
vn.title("Proyectopp")
vn.config(background = "steelblue")
Ventana()

vn.mainloop()