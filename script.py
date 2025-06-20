import tkinter as tk
import ttkbootstrap as ttk
import json
import os
from ttkbootstrap import Style
import tkinter.messagebox as messagebox

def launch_terminal(selected_row, name):
    root.withdraw() 
    terminal(table, selected_row, name) 
    root.deiconify()

def style():    
    style = Style(theme="darkly")
    style.configure("TButton", font=("", 12), padding=10)
    style.configure("TLabel", font=("", 12), padding=10)
    style.configure("Treeview", font=("", 16), rowheight=50)
    return style

def row_selection(event):
    import library as lib
    if lib.important_variables.date == 6:
        messagebox.showinfo("info", "No se puede ingresar felicitaciones o faltas el dia sabado")
        return
    selected_row = table.focus()
    if selected_row:
        name = table.item(selected_row, "values")
        name = name[0]
        print(f"Fila seleccionada: {name}")
        launch_terminal(selected_row, name)

def terminal(table, selected_row, name):        
    terminal = ttk.Toplevel()
    import library as lib
    terminal.title("Añadir falta")
    terminal.geometry("700x500")
    terminal.resizable(False, False)

    ttk.Label(terminal, text="Elige tipo de cara:", font=("Arial", 16)).pack(pady=20)

    button_frame = tk.Frame(terminal)
    button_frame.pack(side="top", pady=20)

    value = tk.BooleanVar()

    button1 = tk.Button(button_frame, command=lambda: (value.set(True), print(value.get())))
    button1.pack(side="left", padx=10)

    lib.animation.animate_emoji(terminal, lib.Gifs.gif_happy, button1, 35)

    button2 = tk.Button(button_frame, command=lambda: (value.set(False), print(value.get())))
    button2.pack(side="left", padx=10)

    lib.animation.animate_emoji(terminal, lib.Gifs.gif_sad, button2, 50)

    textbox = tk.Text(terminal, height=10, width=50)
    textbox.pack(pady=10)
    
    button_ask = ttk.Button(terminal, text="Añadir", command=lambda: lib.add_and_ask.ask(table, selected_row, name, textbox, value))
    button_ask.pack(pady=10)

    terminal.wait_window(terminal)
    
def main_window():
    global root, table
    root = ttk.Window()
    import library as lib
    if not os.path.exists("person.json"):
        lib.json_methods.json_data()
    root.title("Ventana Principal")
    root.geometry("700x600")    
    root.resizable(False, False)
    label = ttk.Label(root, text="Bienvenido a faltas semanales", font=("", 20), anchor="center")
    label.pack(pady=20)
    style()

    table = ttk.Treeview(root, columns=("Nombre", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes"), show="headings")
    for columns in table["columns"]:
        table.heading(columns, text=columns)
        table.column(columns, anchor="center", width=100)
    table.pack(pady=20)

    with open("person.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    
    for subject in lib.important_variables.subject:
        table.insert("", "end", iid=subject, values=(data[subject]["name"], "", "", "", "", ""))

    for subject in data:
        for day, emoji in zip(data[subject]["day"], data[subject]["emoji"]):
            if day == []:
                continue
            value = list(table.item(subject, "values"))
            value[day] = emoji
            table.item(subject, values=value)

    table.pack(padx=20)
    table.bind("<ButtonRelease-1>", row_selection)

    if lib.important_variables.date == 6:
        root.withdraw()
        lib.weekend.show_winner()
        lib.weekend.show_loser()
        root.deiconify()
    elif lib.important_variables.date == 7:
        root.withdraw()
        lib.json_methods.json_data()
        messagebox.showinfo("Info", "Es domingo no se puede acceder(JSON borrado)")
        return

    root.mainloop()

if __name__ == "__main__":
    main_window()  
