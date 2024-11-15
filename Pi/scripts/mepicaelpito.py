from time import sleep
import RPi.GPIO as GPIO

DIR = 13
STEP = 19
CW = 1      #clockwise rotation
CCW = 0     #Counterclockwise rotation
SPR = 200
ENABLE = 12 
MODE  =(16, 17, 20)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)


# Step the motor
def step_motor(direction, steps, delay):
    #Set direction
    GPIO.output(DIR, direction)
    
    #Step the motor
    for _ in range(steps):
       GPIO.output(STEP, GPIO.HIGH)
       sleep(delay)
       GPIO.output(STEP, GPIO.LOW)
       sleep(delay)
       
try:
    step_motor(CW, SPR, 0.005)
    
    sleep(1)
    
    step_motor(CCW, SPR, 0.005)
    
except KeyboardInterrupt:
    print('Program interrupted') 
finally:
    GPIO.cleanup()

GPIO.cleanup()