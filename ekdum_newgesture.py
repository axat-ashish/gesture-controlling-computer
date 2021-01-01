import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui
AS=serial.Serial('COM4',9600) #Create Serial port object called arduinoSerialData
time.sleep(1) #wait for 2 seconds for the communication to get established

while True:
    incoming = str (AS.readline()) #read the serial data and print it as line
    print (incoming)
    if 'Vup' in incoming:
        pyautogui.hotkey('ctrl', 'up')

if 'Vdn' in incoming:
        pyautogui.hotkey('ctrl', 'down')
