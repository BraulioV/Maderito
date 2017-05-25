import serial

ser = serial.Serial('dev/ttyACM0', 9600)
ser.write('s'.encode()) # se encenderá el led
ser.write('p'.encode()) # no se encenderá
