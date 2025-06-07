import tkinter as tk
import ttkbootstrap as ttk
import tkinter.messagebox as messagebox
import datetime
import json
from colorama import Fore, init
from PIL import Image, ImageTk, ImageSequence
import os
import script 



subject = ["Alejandro", "Santiago", "Mateo", "Mirian", "Jonathan"]

def json_data():
    init(autoreset=True)
    global person
    person = {
         "Alejandro": {
                  "faltas": [],
                  "type" : [],
                  "day": [],
                  "emoji": [],
                  "name": "Alejandro"        
         },
         "Santiago": {
                  "faltas": [],
                  "type" : [],
                  "day": [],
                  "emoji": [],
                  "name": "Santiago"
         },
         "Mateo": {
                  "faltas": [],
                  "type" : [],
                  "day": [],
                  "emoji": [],
                  "name": "Mateo"
         },
         "Mirian": {
                  "faltas": [],
                  "type" : [],
                  "day": [],
                  "emoji": [],
                  "name": "Mirian"
         },
         "Jonathan": {
                  "faltas": [],
                  "type" : [],
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

def json_save(name, type):
      data[name]["faltas"].append(fault_details())
      data[name]["type"].append(type)
      data[name]["day"].append(date())
      data[name]["emoji"].append(emoji)
      print(type)

def add_to_table(table, selected_row, name):
      global data, emoji
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
            if emoji == "😃": 
                 json_save(name, type=1)
            else:
                  json_save(name, type=-1)
            table.item(selected_row, values=values)

            with open("person.json", "w", encoding="utf-8") as file:
                  json.dump(data, file, indent=4, ensure_ascii=False)
            print(Fore.GREEN + "✅ Datos añadidos a la tabla y guardados en el archivo JSON")
            messagebox.showinfo("Info", "Felicitacion añadida con éxito." if value.get() == True else "Falta añadida con éxito.")

def ask(table, selected_row, name):
      if fault_details() != "" and value.get() != None:
            if value.get() == True:
                  answer = messagebox.askyesno("Felicitacion", f"¿Estás seguro de que quieres añadir una felicitacion: {fault_details()}?")
                  if answer:
                        add_to_table(table, selected_row, name)
                        textbox.delete("1.0", tk.END)
                        return
            elif value.get() == False:
                  answer = messagebox.askyesno("Falta", f"¿Estás seguro de que quieres añadir una falta: {fault_details()}?")
                  if answer:
                        add_to_table(table, selected_row, name)
                        textbox.delete("1.0", tk.END)
                        return
      else:
            messagebox.showerror("Error", "Por favor, elige felicitacion o falta y escribe")
            return

def animate_happy(happy, index=0):
      button1.configure(image=happy[index])
      root.after(25, animate_happy, happy, (index + 1) % len(happy))

def animate_sad(sad, index=0):
     button2.configure(image=sad[index])
     index = (index + 1) % len(sad)
     root.after(35, animate_sad, sad, index)

def terminal(table, selected_row, name):        
      global textbox, root, value, button1, button2, happy, sad
      root = ttk.Toplevel()
      root.title("Añadir falta")
      root.geometry("700x500")
      root.resizable(False, False)

      ttk.Label(root, text="Elige tipo de cara:", font=("Arial", 16)).pack(pady=20)

      value = tk.BooleanVar()
      button_frame = tk.Frame(root)
      button_frame.pack(side="top", pady=20)

      happy_face = Image.open("imagen1.gif")
      sad_face = Image.open("imagen2.gif")

      happy = [ImageTk.PhotoImage(f.copy().resize((100, 100), Image.Resampling.LANCZOS))for f in ImageSequence.Iterator(happy_face)]
      sad = [ImageTk.PhotoImage(i.copy().resize((100, 100), Image.Resampling.LANCZOS)) for i in ImageSequence.Iterator(sad_face)]

      button1 = tk.Button(button_frame, command=lambda: (value.set(True), print(value.get())))
      button1.pack(side="left", padx=10)
      animate_happy(happy)

      button2 = tk.Button(button_frame, command=lambda: (value.set(False), print(value.get())))
      button2.pack(side="left", padx=10)
      animate_sad(sad)

      textbox = tk.Text(root, height=10, width=50)
      textbox.pack(pady=10)

      button_ask = ttk.Button(root, text="Añadir", command=lambda: ask(table, selected_row, name))
      button_ask.pack(pady=10)

      root.wait_window(root)
