import tkinter as tk
from tkinter import ttk
import serial
import time
import re
from parameters import *
from tkinter.font import Font
import os


# -------------------  Variables -------------------
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1) 


root = tk.Tk()
username_tk=tk.StringVar()
password_tk=tk.StringVar()
number_entry_tk=tk.IntVar()
output_text=tk.StringVar()
arduino_log=tk.StringVar()

log_tittle=tk.StringVar()
length=0
users=[]
next_id=0

# -------------------  Funciones -------------------

def check_database_length():
	with open("passwords.txt","a+") as file:
		lines=file.readlines()
		return(len(lines))
	
def check_users_indatabase():
	with open("passwords.txt","r") as file:
		lines=file.readlines()
		for line in lines:
			line=line.split(",")
			user_id=line[2]


def in_database(name,password):
	password=password+"\n"
	with open("passwords.txt","a+") as file:
		for line in file:
			line=line.split(",")
			if (line[0]==name):
				if (line[1]==password):
					return True

		return False
	
def get_next_id():
	with open("passwords.txt","r") as file:
		lines=file.readlines()
		for line in lines:
			line=line.split(",")
			user_id=line[2]
			user_id=user_id.replace("\n","")
			users.append(user_id)

	users.sort()
	if not users:
		return 1
	else:
		return int(users[-1])+1

def save_password(username,password):
	with open("passwords.txt","a+") as file:
		next_id=get_next_id()
		file.write(f"{username},{password},{next_id}\n")

	output_text.set("usuario guardado")
	write_read(1)

def check_password(name,password):

	if (name==""):
		if(password==""):
			output_text.set("no hay nombre ni contraseña")
			return False
		if(password!=""):
			output_text.set("no hay nombre")
			return False
	if (password=="" and name!=""):
		output_text.set("no hay contraseña")
		return False
	
	return True

def write_read(x): 
	arduino.write(bytes( str(x), 'utf-8')) 
	time.sleep(0.05) 
	data = arduino.readline() 
	return data

def compare_password():
	name=username_tk.get()
	password=password_tk.get()+"\n"

	if not check_password(name,password):
		return
	else:
		output_text.set("Nombre o contraseña no pueden estar vacios")
	
	passed=False
	with open("passwords.txt","r") as file:
		for line in file:
			line=line.split(",")
			if (line[0]==name):
				if (line[1]==password):
					output_text.set("contraseña correcta")
					passed=True
				else:
					output_text.set("contraseña incorrecta")
					return
		output_text.set("no se encontro el usuario")
	if passed:
		write_read(2)

	return

def summit():	
	name=username_tk.get()
	password=password_tk.get()

	


	if (name!="" and password!=""):
		if check_password(name,password):
			if not in_database(name,password):


				username_tk.set("")
				password_tk.set("")
				save_password(name,password)
				
			else:
				output_text.set("el usuario ya existe")

def resize(scale_value):
	scale_value = float(scale_value)

	for widget in root.winfo_children():
		# print(widget.winfo_class())
		if "font" in widget.keys():
			font = widget.cget("font")
			dict_font=tk.font.Font(font=widget["font"]).actual() # diccionario con los valores de la fuente

			size=dict_font["size"]
			# print(size)
			
			widget.configure(font=(font[0], int(scale_value * size)))

		if widget.winfo_class() == 'TButton':
			
			widget.configure(width=int(scale_value * 10))

def read():
	data = arduino.readline().decode().strip()
	if data!="":
		print(data)
		arduino_log.set(data)
	root.after(100,read)



# -------------------  Configuracion de la ventana -------------------
root.title("Sistema de seguridad")
root.iconbitmap("icon.ico")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

scale_ratio=3*screen_width/base_dims[0]
res_x = 400*scale_ratio
res_y = 150*scale_ratio
root.geometry(f"{int(res_x)}x{int(res_y)}")
root.configure(bg=color_bg_300)

# -------------------  Configuracion de estilo -------------------
style = ttk.Style()
style.theme_use('alt')
style.configure("TButton",font=('Helvetica', int(5*scale_ratio )),foreground=color_accent_200)
style.map("TButton", background=[('active',color_primary_100),('!active',color_primary_200)])

# -------------------  Elementos de interfaz -------------------

log_tittle.set("Estatus actual:")


Register_button = ttk.Button(root, text="Entrar",command=summit,style="TButton")
compare_button=ttk.Button(root, text="Comparar",command=compare_password ,style='TButton')

name_entry = tk.Entry(root,textvariable=username_tk)
name_text=tk.Label(root,text="Usuario",bg=color_bg_300,fg=color_text_100)
password_entry = tk.Entry(root,textvariable=password_tk)
password_text=tk.Label(root,text="Contraseña",bg=color_bg_300,fg=color_text_100)
number_entry = tk.Entry(root,textvariable=number_entry_tk)

status_title=tk.Label(root,textvariable=log_tittle,bg=color_bg_300,fg=color_text_100,font=('Helvetica', int(2*scale_ratio )),padx=30,pady=10)
output_label=tk.Label(root,textvariable=output_text,bg=color_bg_300,fg=color_text_100,font=('Helvetica', int(2*scale_ratio )),wraplength=400)
arduino_log_label=tk.Label(root,textvariable=arduino_log,bg=color_bg_300,fg=color_text_100,font=('Helvetica', int(2*scale_ratio )),wraplength=400)

# -------------------  Posicionamiento de elementos -------------------
name_text.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
password_text.grid(row=1,column=0)
password_entry.grid(row=1,column=1)


Register_button.grid(row=2,column=1)
compare_button.grid(row=3,column=1)



status_title.grid(row=0,column=2)
output_label.grid(row=2,column=2,padx=50)
arduino_log_label.grid(row=3,column=2,padx=50)


# -------------------  Ejecucion de la ventana -------------------
length=check_database_length()

if length==0:
	next_id=1
else:
	next_id=get_next_id()

print('next id:',get_next_id())
resize(scale_ratio)

root.after(100,read)
root.mainloop()

print("ran successfully")