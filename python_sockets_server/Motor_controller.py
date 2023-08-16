import RPi.GPIO as GPIO #import gpio pin library from raspbian OS
from time import sleep #importing sleep from python

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, Ena, In1A, In2A, Enb, In1B, In2B):
        #left motor initialization
        self.Ena = Ena
        self.In1A = In1A
        self.In2A = In2A

        #all of the GPIO pins will be declared as an output
        #two of our pins are for our direction
        GPIO.setup(self.Ena, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        self.pwmA = GPIO.PWM(self.Ena, 100);
        self.pwmA.start(0);

        #right motor initialization
        self.Enb = Enb
        self.In1B = In1B
        self.In2B = In2B

        #all of the GPIO pins will be declared as an output
        #two of our pins are for our direction
        GPIO.setup(self.Enb, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)
        self.pwmB = GPIO.PWM(self.Enb, 100);
        self.pwmB.start(0);

    def move(self,speed=0.5, turn=0, t=0): ###############tut function
        #normalizing values
        #0.5 = 50% speed and 1 =  100% speed
        #-1 to 1 will be normalized value for turn
        speed *= 100
        turn *= 100

        #handeling turns
        leftSpeed = speed - turn
        rightSpeed = speed + turn
        if leftSpeed>100:
            leftSpeed=100
        elif leftSpeed<-100:
            leftSpeed=-100
        if rightSpeed>100:
            rightSpeed=100
        elif rightSpeed<-100:
            rightSpeed=-100

        ls = leftSpeed
        rs = rightSpeed

        #left motors movement
        #ChangeDutyCycle do not understand (-ve) sign so we need to use absolute value and the way we can do this is by abs(leftSpeed) this will remove (-ve) sign from the values
        self.pwmA.ChangeDutyCycle(abs(ls));
        if leftSpeed>0:
            GPIO.output(self.In1A, GPIO.HIGH)
            GPIO.output(self.In2A, GPIO.LOW)
        else:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)

        #right motors movement
        self.pwmB.ChangeDutyCycle(abs(rs));
        if rightSpeed>0:
            GPIO.output(self.In1B, GPIO.HIGH)
            GPIO.output(self.In2B, GPIO.LOW)
        else:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)

        sleep(t)
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);

    def forward(self,speed=0.5, t=0):
        speed *= 100
        self.pwmA.ChangeDutyCycle(speed);
        self.pwmB.ChangeDutyCycle(speed);

        #left motors movement forward
        GPIO.output(self.In1A, GPIO.HIGH)
        GPIO.output(self.In2A, GPIO.LOW)
        #right motors movement forward
        GPIO.output(self.In1B, GPIO.HIGH)
        GPIO.output(self.In2B, GPIO.LOW)
        sleep(t)
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);

    def reverse(self,speed=0.5, t=0):
        speed *= 100
        self.pwmA.ChangeDutyCycle(speed);
        self.pwmB.ChangeDutyCycle(speed);

        #left motors movement forward
        GPIO.output(self.In1A, GPIO.LOW)
        GPIO.output(self.In2A, GPIO.HIGH)
        #right motors movement forward
        GPIO.output(self.In1B, GPIO.LOW)
        GPIO.output(self.In2B, GPIO.HIGH)
        sleep(t)
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);

    def left(self,speed=0.5, t=0):
        speed *= 100
        self.pwmA.ChangeDutyCycle(speed);
        self.pwmB.ChangeDutyCycle(speed);

        #left motors movement forward
        GPIO.output(self.In1A, GPIO.HIGH)
        GPIO.output(self.In2A, GPIO.LOW)
        #right motors movement forward
        GPIO.output(self.In1B, GPIO.LOW)
        GPIO.output(self.In2B, GPIO.HIGH)
        sleep(t)
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);

    def right(self,speed=0.5, t=0):
        speed *= 100
        self.pwmA.ChangeDutyCycle(speed);
        self.pwmB.ChangeDutyCycle(speed);

        #left motors movement forward
        GPIO.output(self.In1A, GPIO.LOW)
        GPIO.output(self.In2A, GPIO.HIGH)
        #right motors movement forward
        GPIO.output(self.In1B, GPIO.HIGH)
        GPIO.output(self.In2B, GPIO.LOW)
        sleep(t)
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);

    def stop(self, t=0):
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);
        sleep(t)

#declaring main function
def main():
    #Motor controller testing
    motor.forward(0.50,3)
    motor.stop(5)
    motor.forward(1,3)
    motor.stop(5)

    motor.left(0.50,3)
    motor.stop(5)
    motor.left(1,3)
    motor.stop(5)

    motor.right(0.50,3)
    motor.stop(5)
    motor.right(1,3)
    motor.stop(5)

    motor.reverse(0.50,3)
    motor.stop(5)
    motor.reverse(1,3)
    motor.stop(5)

#it should run if its called alone
#it should also run when main module is calling this module
#THIS CONDITION CHECKS wheather you are running this module or not
if __name__ == '__main__':
    #PASSING PIN NUMBERS TO THE MOTOR CLASS
    #left motors GPIO pin numbers Ena = 12, In1A = 3, In2A = 5
    #right motors GPIO pin numbers Enb = 13, In1B = 11, In2B = 7
    # Motor(Ena, In1A, In2A, Enb, In1B, In2B)
    motor = Motor(12, 3, 5, 13, 11, 7)
    main()
