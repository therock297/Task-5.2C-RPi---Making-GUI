from tkinter import *
import tkinter.font as FONT
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

##Pin Definitions
Red_Led = LED(14)
Yellow_Led = LED(15)
Green_Led = LED(18)


## GUI definitions        
win = Tk()
win.title("LED Toggler")
myFont = FONT.Font(family = 'Helvetica', size = 14, weight = "bold")

##Event Functions
##This method will toggle the red led

var = IntVar()
def led_toggle1():
    if Red_Led.is_lit:
        Red_Led.off()
        Yellow_Led.off()
        Green_Led.off()
    else:
        Red_Led.on()
        Yellow_Led.off()
        Green_Led.off()
         
def led_toggle2():
    if Yellow_Led.is_lit:
        Red_Led.off()
        Yellow_Led.off()
        Green_Led.off()
    else:
        Red_Led.off()
        Yellow_Led.on()
        Green_Led.off()
        
def led_toggle3():
    if Green_Led.is_lit:
        Red_Led.off()
        Yellow_Led.off()
        Green_Led.off()
    else:
        Red_Led.off()
        Yellow_Led.off()
        Green_Led.on()
    
    
##This method destroys the window and sets the GPIO pins back to their internal settings    
def close():
    GPIO.cleanup()
     
##Widgets
    
red_Button = Radiobutton(win, text = "RED LED", font = myFont, command = led_toggle1, bg = 'red', height = 2, width = 24, variable = var, value = 1)
red_Button.grid(row = 1,column = 0)

yellow_Button = Radiobutton(win, text = "YELLOW LED", font = myFont, command = led_toggle2, bg = 'yellow', height = 2, width = 24, variable = var, value = 2)
yellow_Button.grid(row = 1,column = 1)

green_Button = Radiobutton(win, text = "GREEN LED ", font = myFont, command = led_toggle3, bg = 'green', height = 2, width = 24, variable = var, value = 3)
green_Button.grid(row = 1,column = 2)
 
exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'bisque2', height = 1, width = 6)
exitButton.grid(row=2,column=1)

win.protocol("wM_DELETE_WINDOW", close)  #exit cleanly
win.mainloop() #Loop forever


