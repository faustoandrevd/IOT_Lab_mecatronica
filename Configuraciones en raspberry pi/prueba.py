#import GPIO library
import RPi.GPIO as GPIO

#set GPIO numbering mode and define input pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN)

try:
    while True:
        if GPIO.input(5)==0:
            print ("Open")
        else:
            print ("Closed")

finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()
