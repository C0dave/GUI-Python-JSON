import tkinter as tk
import ttkbootstrap as ttk
import library as lib
import json
import os

def return_main():
    return main_window()    

def main_window():
    lib.loser_of_week()
    lib.check_date()
    if not os.path.exists("person.json"):
        lib.json_data() 
    global root
    root = ttk.Window()
    root.title("Ventana Principal")
    root.geometry("500x300")
    root.resizable(False, False)
    label = tk.Label(root, text="Bienvenido a faltas semanales", font=("Arial", 16), bg="lightblue")
    label.pack(pady=20)
    menubutton = tk.Menubutton(root, text="Mirar faltas")
    menubutton.pack(pady=10)
    menu = tk.Menu(menubutton)
    menubutton["menu"] = menu

    menu.add_command(label="Alejandro", command=lambda:(root.destroy(), lib.create_window(0), return_main()))  
    menu.add_command(label="Santiago", command=lambda:(root.destroy(), lib.create_window(1), return_main()))
    menu.add_command(label="Mateo", command=lambda:(root.destroy(), lib.create_window(2), return_main()))
    menu.add_command(label="Mirian", command=lambda:(root.destroy(), lib.create_window(3), return_main()))
    menu.add_command(label="Jonathan", command=lambda:(root.destroy(), lib.create_window(4), return_main()))

    
    table = ttk.Treeview(root, columns=("Nombre", "Faltas"), show="headings")
    table.heading("Nombre", text="Nombre")
    table.heading("Faltas", text="Faltas")

    with open("person.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    for i in data:
       table.insert("", "end", values= (data[i]["name"], data[i]["num_de_faltas"]))  

    table.column("Nombre", width=200, anchor="center")
    table.column("Faltas", width=200, anchor="center")
    table.pack(pady=10) 
    with open("person.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    root.mainloop()

if __name__ == "__main__":
    main_window()