import RPi.GPIO as GPIO
import tkinter as tk

pingID = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pingID, GPIO.OUT)

root = tk.Tk()

def ledOn():
    label.config(text='open')
    GPIO.output(pingID, 1) #open LED

def ledOff():
    label.config(text='close')
    GPIO.output(pingID, 0) #open LED


tk.Button(root, bg='yellow', text='On', command=ledOn).pack()
tk.Button(root, bg='orange', text='Off', command=ledOff).pack()
label = tk.Label(root, text='close')
label.pack()

root.mainloop()
GPIO.cleanup()
