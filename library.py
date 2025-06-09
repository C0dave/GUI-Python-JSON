import tkinter as tk
import ttkbootstrap as ttk
import tkinter.messagebox as messagebox
import datetime
import json
from colorama import Fore, init
from PIL import Image, ImageTk, ImageSequence

subject = ["Alejandro", "Santiago", "Mateo", "Mirian", "Jonathan"]
inner_keys = ["drafting", "type", "day", "emoji", "name"]

def json_data():
      init(autoreset=True)
      global person
      person = {s: {ik:s if ik == "name" else [] for ik in inner_keys} for s in subject}
      with open("person.json", "w", encoding="utf-8") as file:
            json.dump(person, file, indent=4, ensure_ascii=False)
      print(Fore.GREEN + "✅ Archivo JSON creado con éxito")
        
def date():
      day = datetime.datetime.now()
      to_int = day.weekday() + 1
      return to_int

def define_loser_winner(w_or_l):
      with open("person.json", "r", encoding="utf-8") as file:
            sum_type = json.load(file)
      scores = {i: sum(sum_type[i]["type"]) for i in subject}
      loser_ = min(scores)
      winner_ = max(scores)   
      w_or_l.configure(text=f"{winner_ + " es el ganador" if w_or_l == winner_name else loser_ + " es el perdedor"} de la semana", font=("", 20), padding=10)
      return scores

def animate_winner(winner_animation, index=0):
      gif_happy.configure(image=winner_animation[index])
      index = (index + 1) % len(winner_animation)
      gif_happy.after(50, animate_winner, winner_animation, index)

def animate_loser(loser_animation, index=0):
      gif_loser.configure(image=loser_animation[index])
      index = (index + 1) % len(loser_animation)
      gif_loser.after(30, animate_loser, loser_animation, index)

def show_winner_loser():
      global gif_happy, winner_name, gif_loser, loser_name
      winner = ttk.Toplevel()
      winner.title("Ganador")
      winner.geometry("600x400")
      winner.resizable(False, False)
      
      winner_gif = Image.open("imagen3.gif")
      winner_animation = [ImageTk.PhotoImage(w.copy().resize((100, 100), Image.Resampling.LANCZOS)) for w in ImageSequence.Iterator(winner_gif)]

      gif_happy = ttk.Label(winner)
      gif_happy.pack(pady=40)

      animate_winner(winner_animation)

      winner_name = ttk.Label(winner)
      winner_name.pack(pady=20)

      define_loser_winner(winner_name)

      winner.after(5000, winner.destroy)
      winner.wait_window(winner)

      loser = ttk.Toplevel()
      loser.title("Perdedor")
      loser.geometry("600x400")
      loser.resizable(False, False)
      
      loser_gif = Image.open("imagen4.gif")
      loser_animation = [ImageTk.PhotoImage(l.copy().resize((100, 100), Image.Resampling.LANCZOS)) for l in ImageSequence.Iterator(loser_gif)]

      gif_loser = ttk.Label(loser)
      gif_loser.pack(pady=20)

      animate_loser(loser_animation)

      loser_name = ttk.Label(loser)
      loser_name.pack(pady=20)

      define_loser_winner(loser_name)

      loser.after(5000, loser.destroy)
      loser.wait_window(loser)

def fault_details():
   return textbox.get("1.0", tk.END).strip()

def json_save(name, type):
      data[name]["drafting"].append(fault_details())
      data[name]["type"].append(type)
      data[name]["day"].append(date())
      data[name]["emoji"].append(emoji)
      print(type)
      
def json_del(name, index):
      data[name]["day"].pop(index)
      data[name]["type"].pop(index)
      data[name]["drafting"].pop(index)
      data[name]["emoji"].pop(index)

def add_to_table(table, selected_row, name):
      global data, emoji
      init(autoreset=True)
      info = table.item(selected_row, "values")
      values = list(info)
      emoji = "😃" if value.get() == True else "😞"
      values[date()] = emoji
      with open("person.json", "r", encoding="utf-8") as file:
            data = json.load(file)
      if data[name]["day"].count(date()):
            index = data[name]["day"].index(date())
            answer = messagebox.askyesno("Advertencia", f"Ya existe una felicitacion. Detalles:\nTipo: Felicitacion({data[name]["emoji"][index]})\nRedaccion: {data[name]["drafting"][index]}\n¿Quieres reemplazarla?" if data[name]["type"][index] else f"Ya existe una falta. Detalles:\nTipo: Falta({data[name]["emoji"][index]})\nRedaccion: {data[name]["drafting"][index]}\n¿Quieres reemplazarla?")
            if answer:
                  json_del(name, index)
                  json_save(name, type= 1 if value.get() == True else -1)
                  messagebox.showinfo("Info", "Felicitacion reemplazada!" if data[name]["emoji"][index] else "Falta reemplazada!")
                  table.item(selected_row, values=values)
            else:
                  messagebox.showerror("Error", "Accion interrupida por el usuario")
      else:
            if emoji == "😃": 
                  json_save(name, type=1)
            else:
                  json_save(name, type=-1)
            table.item(selected_row, values=values)

      with open("person.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
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
      index = (index + 1) % len(happy)
      root.after(25, animate_happy, happy, index)

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

      happy = [ImageTk.PhotoImage(f.copy().resize((100, 100), Image.Resampling.LANCZOS)) for f in ImageSequence.Iterator(happy_face)]
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