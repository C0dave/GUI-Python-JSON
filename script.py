import tkinter as tk
import ttkbootstrap as ttk
import library as lib
import json
import os
from ttkbootstrap import Style

def return_main():
    return main_window()    

def main_window():
    lib.loser_of_week()
    lib.check_date()
    if not os.path.exists("person.json"):
        lib.json_data() 
    global root
    root = ttk.Window(themename="darkly")
    root.title("Ventana Principal")
    root.geometry("700x600")
    root.resizable(False, False)
    label = ttk.Label(root, text="Bienvenido a faltas semanales", font=(30), anchor="center")
    label.pack(pady=20)

    style = Style()
    style.configure("Treeview", rowheight=40)

    table = ttk.Treeview(root, columns=("Nombre", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes"), show="headings", height=10)
    for col in table["columns"]:
        table.heading(col, text=col)
        table.column(col, anchor="center", width=100)
        table.pack(pady=20)

    with open("person.json", "r") as file:
        data = json.load(file)
    for person in data:
        table.insert("", "end", values=data[person]["name"])
    table.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main_window()