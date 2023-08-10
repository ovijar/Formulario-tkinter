"""Importacion de modulos y librerias"""
#from pymongo import MongoClient
import tkinter as tk
from lista import especies

#  - Conexion 
#cliente = MongoClient("mongodb+srv://ovijar:MeiLing26@cluster0.3z0e7m7.mongodb.net/")
#db = cliente["registro"]
#coleccion = db["ave"]

# - FUNCIONES -
def autocomplete(event):
    """Definiendo la funcion de autocompletado de las especies"""
    text = entry.get().lower()  # Obtén el texto ingresado y conviértelo a minúsculas
    matches = [especie for especie in l_especies 
               if especie.lower().startswith(text)]  # Busca elementos que comienzan con el texto ingresado
    listbox.delete(0, tk.END)  # Borra todos los elementos de la lista

    for match in matches:
        listbox.insert(tk.END, match)  # Agrega los elementos coincidentes a la lista

def select_item():
    """Funcion de integracion del selector de tkinter"""
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        selection_label.config(text="Seleccionado: " + selected_item)

# cantidad
numero = 0
def decrementar():
    global numero
    numero -= 1
    label.config(text=str(numero))

def incrementar():
    global numero
    numero += 1
    label.config(text=str(numero))

root = tk.Tk()
root.title("Registro de aves")
root.geometry("500x800")
mensaje = tk.Label(root, text="Formulario de registros de aves",fg="lightblue")
mensaje.pack(pady=20, )

entry = tk.Entry(root)
entry.pack()
l_especies = especies
listbox = tk.Listbox(root)
listbox.pack()

selection_button = tk.Button(root, text="Seleccionar",fg="green", command=select_item)
selection_button.pack()



selection_label = tk.Label(root, text="Seleccionado: ",fg="cyan")
selection_label.pack()

entry.bind('<KeyRelease>', autocomplete)  
# Asocia el evento de autocompletado a la entrada de texto

lugar_label = tk.Label(root, text = "Lugar:")
lugar_label.pack()
lugar_entry = tk.Entry(root, width=30)
lugar_entry.pack(pady=10)


label_cantidad = tk.Label(root, text="Cantidad")
label_cantidad.pack()
label = tk.Label(root, text=str(numero))
label.pack()
boton_decrementar = tk.Button(root, text=" - ", command=decrementar)
boton_decrementar.pack()
boton_incrementar = tk.Button(root, text=" + ", command=incrementar)
boton_incrementar.pack()

habitat_label = tk.Label(root, text = "Habitat")
habitat_label.pack()
habitat_entry = tk.Entry(root, width=30)
habitat_entry.pack(pady=10)

tipo_de_registro_label = tk.Label(root, text = "Tipo de Registro:")
tipo_de_registro_label.pack()
tipo_de_registro_entry = tk.Entry(root, width=30)
tipo_de_registro_entry.pack(pady=10)

hora_label = tk.Label(root, text="Hora")
hora_label.pack()
hora_label = tk.Entry(root, text="HH:MM")
hora_label.pack()

save_button = tk.Button(root, text="SALVAR")
save_button.pack()

root.mainloop()