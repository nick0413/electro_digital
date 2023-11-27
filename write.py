import tkinter as tk
from tkinter import ttk

'''
    --primary-100:#00BFA5;
    --primary-200:#00a189;
    --primary-300:#005f4b;
    --accent-100:#FF4081;
    --accent-200:#ffe4ff;
    --text-100:#FFFFFF;
    --text-200:#e0e0e0;
    --bg-100:#1A1A1A;
    --bg-200:#292929;
    --bg-300:#404040;
      
      
'''
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


def resize(scale_value):
	scale_value = float(scale_value)
	for widget in root.winfo_children():
		if "font" in widget.keys():
			font = widget.cget("font")
			widget.configure(font=(font[0], int(scale_value * 10)))
		if widget.winfo_class() == 'Button':
			widget.configure(width=int(scale_value * 10))


def summit():
    name=username_tk.get()
    password=password_tk.get()

    username_tk.set("")
    password_tk.set("")

    print(name,password)


# open a tk window
res_x = 800
res_y = 400
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width,screen_height)
style = ttk.Style()
style.theme_use('alt')
style.map('TButton', background=[('active',color_primary_100),('!active',color_primary_200)])
style.configure('TButton',fontscale=5.5,foreground=color_accent_200)

root.title("Arduino COMS")
root.geometry(f"{res_x}x{res_y}")
# change root background color
root.configure(bg=color_bg_300)



username_tk=tk.StringVar()
password_tk=tk.StringVar()

# add a button
button = ttk.Button(root, text="Entrar",command=summit,style='TButton')


name_entry = tk.Entry(root,textvariable=username_tk)
name_text=tk.Label(root,text="Usuario",bg=color_bg_300,fg=color_text_100)
password_entry = tk.Entry(root,textvariable=password_tk)
password_text=tk.Label(root,text="Contraseña",bg=color_bg_300,fg=color_text_100)


name_text.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
password_text.grid(row=1,column=0)
password_entry.grid(row=1,column=1)

button.grid(row=2,column=1)

scale = tk.Scale(root, from_=1, to=10, orient='horizontal', command=resize)
scale.set(1)
scale.grid(row=3, column=0, columnspan=2)
root.mainloop()
root.mainloop()



print("ran successfully")
