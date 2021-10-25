import serial
from art import *
import os

#The following line is for serial over GPIO
port = '/dev/ttyACM0'
#port = 'COM10'

arduino = serial.Serial(port,9600,timeout=100)


while 1:
   
    value = arduino.readline()

    value = int(value.decode("utf-8"))
    
   # print (msg)
   # print( "Hello"+msg+ "Hello")
    #print (value)
    if value ==  1:
        value = str(value)
        tprint("=== "+value+ " ===")
        os.system('rosrun new_test table1.py')

    if value ==  2:
        value = str(value)
        tprint("=== "+value+ " ===")
        os.system('rosrun new_test table2.py')
    if value ==  3:
        value = str(value)
        tprint("=== "+value+ " ===")
	os.system('rosrun new_test table3.py')
    if value ==  4:
        value = str(value)
        tprint("=== "+value+ " ===")
	os.system('rosrun new_test table4.py')
    if value ==  5:
        value = str(value)
        tprint("=== "+value+ " ===")
	os.system('rosrun new_test home.py')
    
else:
    print ("Exiting")

exit()
