import tkinter as tk
import ttkbootstrap as ttk
import tkinter.messagebox as messagebox
import datetime
import json
from colorama import Fore, init
import os

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

def save_json():    
    global subject
    with open("person.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    if subject[num] in data and data != {}:
        data[subject[num]]["faltas"].append(fault_details())
        data[subject[num]]["dia"].append(date())
        data[subject[num]]["num_de_faltas"] = len(data[subject[num]]["faltas"])

        with open("person.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)     
        print(Fore.GREEN + "\n✅ Datos guardados con éxito", Fore.CYAN + "INFO: ", Fore.LIGHTBLUE_EX + "\nRedaccion de falta: ",  fault_details(), Fore.LIGHTBLUE_EX + "\nNumero de falta: ", str(increment_number()), Fore.LIGHTBLUE_EX + "\nDia: ", date(), Fore.LIGHTBLUE_EX + "\nNombre: ", subject[num])
    else:
        print(Fore.RED + "\n❌Error al guardar los datos")

def check_date():
    init(autoreset=True)
    if os.path.exists("person.json"):
        if datetime.datetime.now().weekday() == 5:
            with open("person.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                for i in data:
                  data[i]["faltas"] = []
                  data[i]["dia"] = []
                  data[i]["num_de_faltas"] = 0
                with open("person.json", "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
                print(Fore.GREEN + "\n✅ Datos eliminados con éxito")
        else:
            return 0

def loser_of_week():
    if os.path.exists("person.json"):
        if datetime.datetime.now().weekday() == 5:
            with open("person.json", "r", encoding="utf-8") as file:
                data = json.load(file)
            for i in range(len(data)):
                x = 0
                if data[subject[i]]["num_de_faltas"] == 0:
                    if i == 4:
                        messagebox.showinfo("Perdedor de la semana", "No hay perdedor de la semana")
                        print(Fore.GREEN + ("✅ No hay perdedores esta semana"))
                    else:
                        continue
                else:
                    if data[subject[i]]["num_de_faltas"] == max(data[subject[i]]["num_de_faltas"] for i in range(len(subject))):
                        messagebox.showinfo("Perdedor de la semana",f"El perdedor de la semana es {subject[i]} con {data[subject[i]]['num_de_faltas']} falta/s")
                        print(Fore.GREEN + "\n✅ El perdedor de la semana es ", subject[i], "con", data[subject[i]]["num_de_faltas"], "falta/s")
                        if i == 5:
                            break 
                        else:
                            continue    
        else:
            print(Fore.YELLOW + "\n⚠️ No es fin de semana, no se puede determinar el perdedor de la semana")
            return
    else:
        messagebox.showinfo("Error" , "El Archivo json no esta creado")
        print(Fore.RED + "❌ Archivo json no esta creado")    

def date():
   return datetime.datetime.now().strftime("%A %d de %B de %Y")
 
def fault_details():
   return textbox.get("1.0", tk.END).strip()

def increment_number():
   return len(table.get_children())

def ask():
    if fault_details() == "":
       messagebox.showerror("Error", "No se ha escrito nada.")
       root1.destroy()
    else:
        answer = messagebox.askyesno("Confirmar", f"¿Quieres añadir la falta '{textbox.get('1.0', tk.END).strip()}'?")
        if answer:
            table.insert("", "end", values=(date(), fault_details(), increment_number() + 1)) 
            save_json()
            root1.destroy()
        else:
           messagebox.showinfo("Cancelado", "No se ha añadido la falta.")           
           root1.destroy() 

def add_falta(table):
    global textbox, root1
    root1 = ttk.Window()
    root1.title("Añadir falta")
    root1.geometry("500x300")
    root1.resizable(False, False)

    label = tk.Label(root1, text="Redactar falta", font=("Arial", 16))
    label.pack(pady=20)

    textbox = tk.Text(root1, height=10, width=50)
    textbox.pack(pady=10)

    boton = tk.Button(root1, text="Añadir", command=lambda:(ask()))
    boton.pack(pady=10)

    root1.mainloop()

if __name__ == "__main__":
      add_falta()

def create_window(numero):
    global table, root, num
    num = numero
    root = ttk.Window()
    root.title(subject[num])
    root.geometry("650x450")
    root.resizable(False, False)

    label = tk.Label(root, text="Faltas de la semana", font=("Arial", 16), bg="lightblue")
    label.pack(pady=20)

    table = ttk.Treeview(root, columns=("Fecha", "Falta", "Numero de falta"), show="headings")
    table.heading("Fecha", text="Fecha")
    table.heading("Falta", text="Falta")
    table.heading("Numero de falta", text="Numero de falta")
    table.column("Fecha", width=200, anchor="center")
    table.column("Falta", width=200, anchor="center")   
    table.column("Numero de falta", width=200, anchor="center")
    table.pack(pady=10)

    with open("person.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    for i in range(len(data[subject[num]]["faltas"])):
        table.insert("", "end", values=(data[subject[num]]["dia"][i], data[subject[num]]["faltas"][i], i + 1))
    with open("person.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
       
    boton1 = tk.Button(root, text="Añadir falta", command=lambda:add_falta(table))
    boton1.pack(pady=10)

    check_date()

    root.mainloop()