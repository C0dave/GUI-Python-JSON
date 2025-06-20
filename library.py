import tkinter as tk
import ttkbootstrap as ttk
import tkinter.messagebox as messagebox
import datetime
import json
from colorama import Fore, init
from PIL import Image, ImageTk, ImageSequence
import random

class important_variables:
      subject = ["Alejandro", "Santiago", "Mateo", "Mirian", "Jonathan"]
      inner_keys = ["name", "drafting", "type", "day", "emoji"]
      date = datetime.datetime.now().weekday() + 1   
      def __init__(self, drafting_details):
            self.drafting_details = drafting_details
      
class add_and_ask:
      def add_to_table(table, selected_row, name, value, draf):
            with open("person.json", "r", encoding="utf-8") as file:
                  data = json.load(file)
            info = table.item(selected_row, "values")
            values = list(info)
            emoji = "😃" if value.get() == True else "😞"
            values[important_variables.date] = emoji
            if data[name]["day"].count(important_variables.date):
                  index = data[name]["day"].index(important_variables.date)
                  answer = messagebox.askyesno("Advertencia", f"Ya existe una felicitacion. Detalles:\nTipo: Felicitacion({data[name]["emoji"][index]})\nRedaccion: {data[name]["drafting"][index]}\n¿Quieres reemplazarla?" if data[name]["type"][index] else f"Ya existe una falta. Detalles:\nTipo: Falta({data[name]["emoji"][index]})\nRedaccion: {data[name]["drafting"][index]}\n¿Quieres reemplazarla?")
                  if answer:
                        json_methods.json_del(name, index, data)
                        json_methods.json_save(name, data, draf.drafting_details, emoji, tipe=1 if emoji == "😃" else -1)
                        messagebox.showinfo("Info", "Felicitacion reemplazada!" if data[name]["emoji"][index] else "Falta reemplazada!")
                        table.item(selected_row, values=values)
                  else:
                        messagebox.showerror("Error", "Accion interrupida por el usuario")
                        return
            elif emoji:
                        json_methods.json_save(name, data, draf.drafting_details, emoji, tipe=1 if emoji == "😃" else -1)
                        table.item(selected_row, values=values)

            with open("person.json", "w", encoding="utf-8") as file:
                  json.dump(data, file, indent=4, ensure_ascii=False)
            messagebox.showinfo("Info", "Felicitacion añadida con éxito." if value.get() == True else "Falta añadida con éxito.")
      
      def ask(table, selected_row, name, textbox, value):
            draf = important_variables(textbox.get("1.0", tk.END).strip())
            if draf.drafting_details != "" and value.get() != None:
                  title = ("Felicitacion" if value.get() == True else "Falta")
                  message = (f"¿Estás seguro de que quieres añadir la felicitacion: {draf.drafting_details}?" if value.get() == True else f"¿Estás seguro de que quieres añadir la falta: {draf.drafting_details}?")
                  answer = messagebox.askyesno(title, message)
                  if answer:
                        add_and_ask.add_to_table(table, selected_row, name, value, draf)
                        textbox.delete("1.0", tk.END)
                        return
            else:
                  messagebox.showerror("Error", "Por favor, elige felicitacion o falta y escribe")
                  return
      
class json_methods:
      def json_data():
            init(autoreset=True)
            person = {subject: {inner_keys:subject if inner_keys == "name" else [] for inner_keys in important_variables.inner_keys} if subject != "Validation" else False for subject in important_variables.subject}
            with open("person.json", "w", encoding="utf-8") as file:
                  json.dump(person, file, indent=4, ensure_ascii=False)
            print(Fore.GREEN + "✅ Archivo JSON creado con éxito" if important_variables.date != 1 else Fore.RED + "JSON borrado(Fin de semana)")

      def json_del(name, index, data):
            data[name]["day"].pop(index)
            data[name]["type"].pop(index)
            data[name]["drafting"].pop(index)
            data[name]["emoji"].pop(index)

      def json_save(name, data, draf, emoji, tipe):
            data[name]["drafting"].append(draf)
            data[name]["type"].append(tipe)
            data[name]["day"].append(important_variables.date)
            data[name]["emoji"].append(emoji)
            print(tipe, emoji)

class Gifs:
      gif_happy = [ImageTk.PhotoImage(gh.copy().resize((100, 100), Image.Resampling.LANCZOS)) for gh in ImageSequence.Iterator(Image.open("happy.gif"))]
      gif_sad = [ImageTk.PhotoImage(gs.copy().resize((100, 100), Image.Resampling.LANCZOS)) for gs in ImageSequence.Iterator(Image.open("sad.gif"))]
      gif_celebrate = [ImageTk.PhotoImage(cb.copy().resize((100, 100), Image.Resampling.LANCZOS)) for cb in ImageSequence.Iterator(Image.open("celebrate.gif"))]
      gif_cry = [ImageTk.PhotoImage(cry.copy().resize((100, 100), Image.Resampling.LANCZOS)) for cry in ImageSequence.Iterator(Image.open("crying.gif"))]
      gif_bg_celebrate = [ImageTk.PhotoImage(bgc.copy().resize((600, 400), Image.Resampling.LANCZOS)) for bgc in ImageSequence.Iterator(Image.open("celebration.webp"))]
      gif_bg_thumb_down = [ImageTk.PhotoImage(td.copy().resize((600, 400), Image.Resampling.LANCZOS)) for td in ImageSequence.Iterator(Image.open("thumb_down.gif"))]
      
class animation:
      def animate_emoji(window, gif, type_widget, duration, index=0):
            type_widget.configure(image=gif[index])
            index = (index + 1) % len(gif)
            window.after(duration, animation.animate_emoji, window, gif, type_widget, duration, index)
      
      def animate_bg(window, gif, type_widget, bg, bg_emoji, index=0):
            colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'cyan', 'magenta', 'white']
            fonts = ["Arial", "Helvetica", "Times New Roman", "Courier New", "Verdana", "Comic Sans MS", "Georgia", "Trebuchet MS", "Lucida Console", "Tahoma", "Segoe UI", "System"]
            sizes = list(range(10, 30))
            color_random = random.choice(colors)
            backcolor_random = random.choice(colors)
            font_random = random.choice(fonts)
            size_random = random.choice(sizes)
            bg.configure(image=gif[index])
            bg_emoji.configure(background=backcolor_random)
            type_widget.configure(background=backcolor_random, foreground=color_random, font=(font_random, size_random))
            window.after(100, animation.animate_bg, window, gif, type_widget, bg, bg_emoji, (index + 1) % len(gif))

class weekend:
      def show_winner():
            global winner_name
            winner = ttk.Toplevel()
            winner.title("Ganador")
            winner.geometry("600x400")
            winner.resizable(False, False)

            bg_winner = tk.Label(winner)
            bg_winner.place(x=0, y=0, relwidth=1, relheight=1)

            gif_winner = ttk.Label(winner)
            gif_winner.pack(pady=40)

            animation.animate_emoji(winner, Gifs.gif_celebrate, gif_winner, 50)

            winner_name = ttk.Label(winner)
            winner_name.pack(pady=20)

            weekend.define_loser_winner(winner_name)
            animation.animate_bg(winner, Gifs.gif_bg_celebrate, winner_name, bg_winner, gif_winner)

            winner.after(5000, winner.destroy)
            winner.wait_window(winner)

      def show_loser():
            loser = ttk.Toplevel()
            loser.title("Perdedor")
            loser.geometry("600x400")
            loser.resizable(False, False)

            bg_loser = tk.Label(loser)
            bg_loser.place(x=0, y=0, relwidth=1, relheight=1)

            gif_loser = ttk.Label(loser)
            gif_loser.pack(pady=20)

            loser_name = ttk.Label(loser)
            loser_name.pack(pady=20)

            animation.animate_emoji(loser, Gifs.gif_cry, gif_loser, 50)
            animation.animate_bg(loser, Gifs.gif_bg_thumb_down, loser_name, bg_loser, gif_loser)
            weekend.define_loser_winner(loser_name)

            loser.after(5000, loser.destroy)
            loser.wait_window(loser)

      def define_loser_winner(type_widget):
            with open("person.json", "r", encoding="utf-8") as file:
                  sum_type = json.load(file)
            scores = {i:sum(sum_type[i]["type"]) for i in important_variables.subject}
            winner_ = max(scores, key=scores.get)
            loser_ = min(scores, key=scores.get) 
            type_widget.configure(text=f"{winner_} es el ganador " if type_widget == winner_name else f"{loser_} es el perdedor" + " de la semana", font=("", 20), padding=10)