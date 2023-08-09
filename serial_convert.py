import serial 
from threading import Thread

ser_1 = serial.Serial('/dev/ttyACM0', 250000)
ser_2 = serial.Serial('/dev/ttyV0', 115200)

def read_1_write_2():
    while True:
        data = ser_1.read()
        ser_2.write(data)

def read_2_write_1():
    while True:
        data = ser_2.read()
        ser_1.write(data)
        
Thread(target=read_1_write_2).start()
Thread(target=read_2_write_1).start()
