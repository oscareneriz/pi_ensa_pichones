from time import sleep
import RPi.GPIO as GPIO

DIR = 13
STEP = 19
CW = 1      #clockwise rotation
CCW = 0     #Counterclockwise rotation
SPR = 200
ENABLE = 12 
MODE  = (16, 17, 20)

# DIR = 24
# STEP = 18
# CW = 1      #clockwise rotation
# CCW = 0     #Counterclockwise rotation
# SPR = 200
# ENABLE = 4 
# MODE  = (21, 22, 27)


# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(ENABLE, GPIO.OUT)

GPIO.output(ENABLE, 0)
GPIO.output(DIR, CW)

#Step the motor
for _ in range(5):
   GPIO.output(STEP, GPIO.HIGH)
   print('HIGH')
   sleep(1)
   GPIO.output(STEP, GPIO.LOW)
   print('LOW')
   sleep(1)
       


GPIO.cleanup()
print("CLEANED GPIO")