import time
import serial
ser=serial.Serial('/dev/ttyAMA0', baudrate=9600, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
time.sleep(1)
while True:
    if ser.inWaiting() >0:
        data=ser.read()
        za=data.decode('utf-8')
        #print (data, end="")
        print(za, end=" ")
        
