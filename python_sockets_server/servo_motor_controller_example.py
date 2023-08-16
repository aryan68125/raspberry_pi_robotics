import RPi.GPIO as GPIO
import pigpio
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

# Set up pigpio
pi = pigpio.pi()

# Define function to set servo position
def set_servo_position(pin, position):
    pi.set_servo_pulsewidth(pin, position)

# Move servo 1 to position 0 degrees
set_servo_position(17, 500)

# Move servo 2 to position 90 degrees
set_servo_position(18, 1500)

# Wait for 1 second
time.sleep(1)

# Move servo 1 to position 90 degrees
set_servo_position(17, 1500)

# Move servo 2 to position 180 degrees
set_servo_position(18, 2500)

# Wait for 1 second
time.sleep(1)

# Stop pigpio
pi.stop()

# Clean up GPIO
GPIO.cleanup()
