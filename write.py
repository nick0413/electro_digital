import tkinter as tk
from tkinter import ttk
import serial
import time
arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1) 



color_primary_100="#00BFA5"
color_primary_200="#00a189"
color_primary_300="#005f4b"
color_accent_100="#FF4081"
color_accent_200="#ffe4ff"
color_text_100="#FFFFFF"
color_text_200="#e0e0e0"
color_bg_100="#1A1A1A"
color_bg_200="#292929"
color_bg_300="#404040"

def write_read(x): 
	print(x)
	arduino.write(bytes( str(x), 'utf-8')) 
	time.sleep(0.05) 
	data = arduino.readline() 
	return int(data)


def resize(scale_value):
	scale_value = float(scale_value)

	for widget in root.winfo_children():
		print(widget.winfo_class())
		if "font" in widget.keys():
			font = widget.cget("font")
			widget.configure(font=(font[0], int(scale_value * 10)))
		if widget.winfo_class() == 'TButton':
			
			widget.configure(width=int(scale_value * 10))



def save_password(username,password):
	with open("passwords.txt","a") as file:
		file.write(f"{username},{password}\n")
	
def compare_password():
	name=username_tk.get()
	password=password_tk.get()+"\n"

	if (name=="" or password==""):
		print("no hay nombre ni contraseña")
		return
	
	with open("passwords.txt","r") as file:
		for line in file:
			line=line.split(",")
			if (line[0]==name):
				if (line[1]==password):
					print("contraseña correcta")
					return
				else:
					print("contraseña incorrecta")
					return
		print("no se encontro el usuario")
		return

def summit():	
	name=username_tk.get()
	password=password_tk.get()

	if (name==""):
		if(password==""):
			print("no hay nombre ni contraseña")
		if(password!=""):
			print("no hay nombre")
	if (password=="" and name!=""):
		print("no hay contraseña")
		return

	username_tk.set("")
	password_tk.set("")

	print(name,password)
	if (name!="" and password!=""):
		save_password(name,password)


res_x = 800
res_y = 400
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
base_dims=(2560,1440)
scale_ratio=3*screen_width/base_dims[0]
print(screen_width,screen_height)
print(scale_ratio)
style = ttk.Style()
style.theme_use('alt')
style.map('TButton', background=[('active',color_primary_100),('!active',color_primary_200)])
style.configure('TButton',font=('Helvetica', int(5*scale_ratio )),foreground=color_accent_200)

root.title("Arduino COMS")
root.geometry(f"{int(res_x)}x{int(res_y)}")
# change root background color
root.configure(bg=color_bg_300)



username_tk=tk.StringVar()
password_tk=tk.StringVar()
number_entry_tk=tk.IntVar()
output_text=tk.StringVar()

output_text.set("xd")

button = ttk.Button(root, text="Entrar",command=summit,style='TButton')
compare_button=ttk.Button(root, text="Comparar",command=compare_password ,style='TButton')

name_entry = tk.Entry(root,textvariable=username_tk)
name_text=tk.Label(root,text="Usuario",bg=color_bg_300,fg=color_text_100)
password_entry = tk.Entry(root,textvariable=password_tk)
password_text=tk.Label(root,text="Contraseña",bg=color_bg_300,fg=color_text_100)
number_entry = tk.Entry(root,textvariable=number_entry_tk)
number_pass=ttk.Button(root,text='enviar arduino',command=lambda:write_read(number_entry_tk.get()),style='TButton')
output_label=tk.Label(root,textvariable=output_text,bg=color_bg_300,fg=color_text_100)


name_text.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
password_text.grid(row=1,column=0)
password_entry.grid(row=1,column=1)
button.grid(row=2,column=1)
compare_button.grid(row=3,column=1)
output_label.grid(row=2,column=2)

number_entry.grid(row=4,column=1)
number_pass.grid(row=5,column=1)

resize(scale_ratio)

root.mainloop()



print("ran successfully")
