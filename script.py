import tkinter as tk
import ttkbootstrap as ttk
import library as lib
import json
import os
from ttkbootstrap import Style

def launch_terminal(name):
    root.withdraw() 
    lib.terminal(table, selected_row, name) 
    root.deiconify()

def style():
    style = Style(theme="darkly")
    style.configure("TButton", font=("", 12), padding=10)
    style.configure("TLabel", font=("", 12), padding=10)
    style.configure("Treeview", font=("", 16), rowheight=50)
    return style

def row_selection(event):
    global selected_row
    selected_row = table.focus()
    if selected_row:
        name = table.item(selected_row, "values")
        name = name[0]
        print(f"Fila seleccionada: {name}")
        launch_terminal(name)
    
def main_window():
    global root, table
    if not os.path.exists("person.json"):
        lib.json_data() 
    root = ttk.Window()
    style()
    root.title("Ventana Principal")
    root.geometry("700x600")    
    root.resizable(False, False)
    label = ttk.Label(root, text="Bienvenido a faltas semanales", font=("", 20), anchor="center")
    label.pack(pady=20)

    table = ttk.Treeview(root, columns=("Nombre", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes"), show="headings")
    for col in table["columns"]:
        table.heading(col, text=col)
        table.column(col, anchor="center", width=100)
    table.pack(pady=20)

    with open("person.json", "r") as file:
        data = json.load(file)
    for person in data:
        table.insert("", "end", iid=person, values=(data[person]["name"], "", "", "", "", ""))
    table.pack(pady=20)

    table.bind("<ButtonRelease-1>", row_selection)

    root.mainloop()

if __name__ == "__main__":
    main_window()