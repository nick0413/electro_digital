import serial 
import time 

serial_coms=serial.Serial("COM7",9600)

serial_coms.timeout=0.1


while True:
    i=input("ingrese un comando: ").strip()
    if i=="terminar":
        print("terminando")
        break

    serial_coms.write(i.encode())

    time.sleep(0.1)
    print(serial_coms.readline().decode("ascii"))

serial_coms.close()