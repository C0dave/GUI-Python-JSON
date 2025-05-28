import tkinter as tk
import ttkbootstrap as ttk
import tkinter.messagebox as messagebox
import datetime
import json
from colorama import Fore, init
from PIL import Image, ImageTk
import os
import script 


subject = ["Alejandro", "Santiago", "Mateo", "Mirian", "Jonathan"]

def json_data():
    init(autoreset=True)
    global person
    person = {
         "Alejandro": {
               "faltas": [],
               "dia": [],
               "num_de_faltas": 0,
               "name": "Alejandro"        
         },
         "Santiago": {
               "faltas": [],
               "dia": [],
               "num_de_faltas": 0,
                "name": "Santiago"
         },
         "Mateo": {
               "faltas": [],
               "dia": [],
               "num_de_faltas": 0,
               "name": "Mateo"
         },
         "Mirian": {
               "faltas": [],
               "dia": [],
               "num_de_faltas": 0,
               "name": "Mirian"
         },
         "Jonathan": {
               "faltas": [],
               "dia": [],
               "num_de_faltas": 0,
               "name": "Jonathan"
         }
    }
    if not os.path.exists("person.json"):
        with open("person.json", "w", encoding="utf-8") as file:
            json.dump(person, file, indent=4, ensure_ascii=False)
            print(Fore.GREEN + "✅ Archivo JSON creado con éxito")
    else:
        print(Fore.YELLOW + "\n⚠️ El archivo JSON ya existe")
   
def date():
      day = datetime.datetime.now()
      to_int = day.weekday() + 1
      return to_int

def fault_details():
   return textbox.get("1.0", tk.END).strip()

def add_to_table(table, selected_row):
      info = table.item(selected_row, "values")
      values = list(info)
      values[date()] = "semanal"
      table.item(selected_row, values=values)

def ask(table, selected_row):
      if fault_details() != "":
            if value.get() is True:
                 answer = messagebox.askyesno("Felicitacion", f"¿Estás seguro de que quieres añadir una felicitacion: {fault_details()}?")
                 if answer:
                        messagebox.showinfo("Info", "Felicitacion añadida con éxito.")
                        textbox.delete("1.0", tk.END)
                        add_to_table(table, selected_row)
                        return
            else:
                 answer = messagebox.askyesno("Falta", f"¿Estás seguro de que quieres añadir una falta: {fault_details()}?")
                 if answer:
                        messagebox.showinfo("Info", "Falta añadida con éxito.")
                        textbox.delete("1.0", tk.END)
                        add_to_table(table, selected_row)
                        return
      else:
            messagebox.showerror("Error", "Por favor, escribe una falta o felicitacion antes de continuar.")
            return

def terminal(table, selected_row):        
    global textbox, root, value, photo, photo2
    root = ttk.Toplevel()
    root.title("Añadir falta")
    root.geometry("700x500")
    root.resizable(False, False)

    label = ttk.Label(root, text="Elige tipo de cara:", font=("Arial", 16))
    label.pack(pady=20)

    value = tk.BooleanVar()

    button_frame = tk.Frame(root)
    button_frame.pack(side="top", pady=20)

    image = Image.open("imagen1.jpg").resize((100, 100))
    photo = ImageTk.PhotoImage(image)
    image2 = Image.open("imagen2.png").resize((100, 100))
    photo2 = ImageTk.PhotoImage(image2)

    button1 = tk.Button(button_frame, image=photo, command=lambda:(value.set(True), print(value.get())))
    button1.pack(side="left", padx=10)

    button2 = tk.Button(button_frame, image=photo2, command=lambda:(value.set(False), print(value.get())))
    button2.pack(side="left", padx=10)

    textbox = tk.Text(root, height=10, width=50)
    textbox.pack(pady=10)

    boton = tk.Button(root, text="Añadir", command=lambda: ask(table=table, selected_row=selected_row))
    boton.pack(pady=10)

    root.wait_window(root)
