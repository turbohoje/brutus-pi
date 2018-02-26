#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import ConfigParser

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

touch = GPIO.PWM(11, 50)
touch.start( 7.5 )

slide = GPIO.PWM(13, 50)
slide.start( 2 )

arm = GPIO.PWM(15, 50)
arm.start(7.5)


def setServo(s, pos):
    #print "setting location to %f" % (pos)
    s.ChangeDutyCycle(pos)

def pressButton():
    setServo(touch, pin_11_down)
    time.sleep(0.35)
    setServo(touch, pin_11_up)
    time.sleep(0.35)

def liftFinger():
    setServo(touch, pin_11_up)
    time.sleep(0.5)

def seek(key):
    setServo(slide, 2)
    time.sleep(0.5)

    if key == "C": 
        print "Cancel"
        setServo(arm, 5.3)
        setServo(slide, 7.0)
    if key == "W": #done
        print "get woke"
        setServo(arm, 4.37)
        setServo(slide, 3.7) 
        pressButton()
    if key == "0": #done 
        print "0"
        setServo(arm, 5.0)
        setServo(slide, 6.1) 
    if key == "1": #done
        print "1"
        setServo(arm, 4.2)
        setServo(slide, 10.5)
    if key == "2": #done
        print "2"
        setServo(arm, 4.12)
        setServo(slide, 7.78)
    if key == "3": #done
        print "3"
        setServo(arm, 4.17)
        setServo(slide, 6.4)
    if key == "4": #done
        print "4"
        setServo(arm, 4.6)
        setServo(slide, 7.0)
    if key == "5": #done
        print "5"
        setServo(arm, 4.4)
        setServo(slide, 6.2)
    if key == "6": #done
        print "6"
        setServo(arm, 4.5)
        setServo(slide,4.95) 
    if key == "7": #done
        print "7"
        setServo(arm, 4.87)
        setServo(slide, 6.0)
    if key == "8": #done
        print "8"
        setServo(arm, 4.77)
        setServo(slide, 5.8)
    if key == "9":
        print "9"
        setServo(arm, 4.78)
        setServo(slide, 2.5)
    
    time.sleep(0.5)
    pressButton()

    #hunt from same side
    #setServo(slide, 2)
    time.sleep(0.5)
    return

def seekPic():
    setServo(slide,12)
    setServo(arm, 12)
    time.sleep(0.5)

config = ConfigParser.ConfigParser()

config.read("myconfig.ini")
pin_11_down = float(config.get("myvars", "pin_11_down"))
pin_11_up   = float(config.get("myvars", "pin_11_up"))

liftFinger()

seek("W")
seek("7")
seek("8")
seek("9")
seek("0")


seekPic()

seek("C")
seekPic()

touch.stop()
slide.stop()
arm.stop()
GPIO.cleanup()

print "done"
exit(0)
try:
    while True:
        config.read("myconfig.ini")
        pin_11_down = float(config.get("myvars", "pin_11_down"))
        pin_11_up   = float(config.get("myvars", "pin_11_up"))
        
        slide_ok    = float(config.get("myvars", "slide_ok"))
        slide_out   = float(config.get("myvars", "slide_out"))

        arm_ok      = float(config.get("myvars", "arm_ok"))
        arm_off     = float(config.get("myvars", "arm_off"))


        #setServo(touch, pin_11_down)
        setServo(slide, slide_ok)
        #setServo(arm, arm_off)
        time.sleep(1)
        
        #setServo(touch, pin_11_up)
        setServo(slide, slide_out)
        #setServo(arm, arm_ok )
        pressButton()

        time.sleep(1)



except KeyboardInterrupt:
    touch.stop()
    slide.stop
    arm.stop()
    GPIO.cleanup()


