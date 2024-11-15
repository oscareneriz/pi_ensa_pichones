import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the stepper motor
A1_PIN = 17
B1_PIN = 18
A2_PIN = 22
B2_PIN = 23

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(A1_PIN, GPIO.OUT)
GPIO.setup(B1_PIN, GPIO.OUT)
GPIO.setup(A2_PIN, GPIO.OUT)
GPIO.setup(B2_PIN, GPIO.OUT)

# Define the step sequence for the stepper motor
step_sequence = [
    [1, 0, 1, 0],  # A1 and A2
    [0, 1, 1, 0],  # B1 and A2
    [0, 1, 0, 1],  # B1 and B2
    [1, 0, 0, 1]   # A1 and B2
]

# Function to set the step state of the motor
def set_step(pins_state):
    GPIO.output(A1_PIN, pins_state[0])
    GPIO.output(B1_PIN, pins_state[1])
    GPIO.output(A2_PIN, pins_state[2])
    GPIO.output(B2_PIN, pins_state[3])
    print(f"Setting step: {pins_state}")  # Debugging print statement

# Main loop to control the motor
try:
    while True:
        for step in step_sequence:
            set_step(step)
            time.sleep(1)  # Adjust delay as needed for visible movement
        
except KeyboardInterrupt:
    GPIO.cleanup()  # Ensure GPIO is cleaned up on exit
    print("GPIO cleanup complete.")
