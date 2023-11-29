import tkinter as tk
import serial
import time

arduino = serial.Serial(port = "COM7", baudrate = 115200, timeout = None)
time.sleep(2)

def LEDON1():
    arduino.write(b"2")
def LEDON2():
    arduino.write(b"3")
def LEDON3():
    arduino.write(b"4")
def LEDON4():
    arduino.write(b"5")

def LEDOFF():
    arduino.write(b"1")
    
window = tk.Tk()
window.title("LED CONTROL CENTER")
# button0= tk.Button(window, text = "LED 1", command = LEDON1)
button = tk.Button(text = "LED 1", command = LEDON1)
button2 = tk.Button(text = "LED 2", command = LEDON2)
button3 = tk.Button(text = "LED 3", command = LEDON3)
button4 = tk.Button(text = "LED 4", command = LEDON4)
button5 = tk.Button(text = "ALL off", command = LEDOFF)

button.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

window.mainloop()