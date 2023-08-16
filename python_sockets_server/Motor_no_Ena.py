import RPi.GPIO as GPIO #import gpio pin library from raspbian OS
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, In1A, In2A, In1B, In2B):
        #left motor initialization
        self.In1A = In1A
        self.In2A = In2A

        #all of the GPIO pins will be declared as an output
        #two of our pins are for our direction
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)

        #right motor initialization
        self.In1B = In1B
        self.In2B = In2B

        #all of the GPIO pins will be declared as an output
        #two of our pins are for our direction
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)

    def forward(self):
        #left motors movement forward
        GPIO.output(self.In1A, GPIO.HIGH)
        GPIO.output(self.In2A, GPIO.LOW)
        #right motors movement forward
        GPIO.output(self.In1B, GPIO.HIGH)
        GPIO.output(self.In2B, GPIO.LOW)

    def reverse(self):
        #left motors movement forward
        GPIO.output(self.In1A, GPIO.LOW)
        GPIO.output(self.In2A, GPIO.HIGH)
        #right motors movement forward
        GPIO.output(self.In1B, GPIO.LOW)
        GPIO.output(self.In2B, GPIO.HIGH)

    def left(self):
        #left motors movement forward
        GPIO.output(self.In1A, GPIO.HIGH)
        GPIO.output(self.In2A, GPIO.LOW)
        #right motors movement forward
        GPIO.output(self.In1B, GPIO.LOW)
        GPIO.output(self.In2B, GPIO.HIGH)

    def right(self):
        #left motors movement forward
        GPIO.output(self.In1A, GPIO.LOW)
        GPIO.output(self.In2A, GPIO.HIGH)
        #right motors movement forward
        GPIO.output(self.In1B, GPIO.HIGH)
        GPIO.output(self.In2B, GPIO.LOW)

    def stop(self):
        #left motors movement forward
        GPIO.output(self.In1A, GPIO.LOW)
        GPIO.output(self.In2A, GPIO.LOW)
        #right motors movement forward
        GPIO.output(self.In1B, GPIO.LOW)
        GPIO.output(self.In2B, GPIO.LOW)

#declaring main function
def main():
    #Motor controller testing
    motor.forward()
    sleep(2)
    motor.stop()
    sleep(2)
    motor.left()
    sleep(2)
    motor.stop()
    sleep(2)
    motor.right()
    sleep(2)
    motor.stop()
    sleep(2)
    motor.reverse()
    sleep(2)
    motor.stop()

#it should run if its called alone
#it should also run when main module is calling this module
#THIS CONDITION CHECKS wheather you are running this module or not
if __name__ == '__main__':
    #PASSING PIN NUMBERS TO THE MOTOR CLASS
    #left motors GPIO pin numbers Ena = 12, In1A = 3, In2A = 5
    #right motors GPIO pin numbers Enb = 13, In1B = 11, In2B = 7
    # Motor( In1A, In2A, In1B, In2B)
    motor = Motor( 3, 5, 11, 7)
    main()
