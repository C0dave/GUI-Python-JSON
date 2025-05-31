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
                  "day": [],
                  "emoji": [],
                  "name": "Alejandro"        
         },
         "Santiago": {
                  "faltas": [],
                  "day": [],
                  "emoji": [],
                  "name": "Santiago"
         },
         "Mateo": {
                  "faltas": [],
                  "day": [],
                  "emoji": [],
                  "name": "Mateo"
         },
         "Mateo": {
                  "faltas": [],
                  "day": [],
                  "emoji": [],
                  "name": "Mateo"
         },
         "Mirian": {
                  "faltas": [],
                  "day": [],
                  "emoji": [],
                  "name": "Mirian"
         },
         "Jonathan": {
                  "faltas": [],
                  "day": [],
                  "emoji": [],
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

def add_to_table(table, selected_row, name):
      with open("person.json", "r", encoding="utf-8") as file:
            data = json.load(file)
      if data[name]["day"].count(date()):
            messagebox.showwarning("Advertencia", "⚠️ Ya existe una falta o felicitacion para este dia")
            return
      else:
            init(autoreset=True)
            info = table.item(selected_row, "values")
            values = list(info)
            emoji = "😃" if value.get() == True else "😞"
            values[date()] = emoji
            table.item(selected_row, values=values)
            data[name]["faltas"].append(fault_details())
            data[name]["day"].append(date())
            data[name]["emoji"].append(emoji)
            with open("person.json", "w", encoding="utf-8") as file:
                  json.dump(data, file, indent=4, ensure_ascii=False)
            print(Fore.GREEN + "✅ Datos añadidos a la tabla y guardados en el archivo JSON")
            messagebox.showinfo("Info", "Felicitacion añadida con éxito." if value.get() == True else "Falta añadida con éxito.")


def ask(table, selected_row, name):
      if fault_details() != "":
            if value.get() == True:
                 answer = messagebox.askyesno("Felicitacion", f"¿Estás seguro de que quieres añadir una felicitacion: {fault_details()}?")
                 if answer:
                        add_to_table(table, selected_row, name)
                        textbox.delete("1.0", tk.END)
                        return
            else:
                 answer = messagebox.askyesno("Falta", f"¿Estás seguro de que quieres añadir una falta: {fault_details()}?")
                 if answer:
                        add_to_table(table, selected_row, name)
                        textbox.delete("1.0", tk.END)
                        return
      else:
            messagebox.showerror("Error", "Por favor, escribe una falta o felicitacion antes de continuar.")
            return

def terminal(table, selected_row, name):        
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
    image2 = Image.open("imagen2.jpg").resize((100, 100))
    photo2 = ImageTk.PhotoImage(image2)

    button1 = tk.Button(button_frame, image=photo, command=lambda:(value.set(True), print(value.get())))
    button1.pack(side="left", padx=10)

    button2 = tk.Button(button_frame, image=photo2, command=lambda:(value.set(False), print(value.get())))
    button2.pack(side="left", padx=10)

    textbox = tk.Text(root, height=10, width=50)
    textbox.pack(pady=10)

    boton = tk.Button(root, text="Añadir", command=lambda: ask(table=table, selected_row=selected_row, name=name))
    boton.pack(pady=10)

    root.wait_window(root)
