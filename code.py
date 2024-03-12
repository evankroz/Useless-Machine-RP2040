import random
import time
import board
import pwmio
import digitalio
from adafruit_motor import servo


pwm_servo12= pwmio.PWMOut(board.GP12, frequency=50)
servo12 = servo.Servo(pwm_servo12)
pwm_servo15 = pwmio.PWMOut(board.GP15, frequency=50)
servo15 = servo.Servo(pwm_servo15)
switch = digitalio.DigitalInOut(board.GP0)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN

servo12.angle = 0
servo15.angle = 15

def move(servo, target_angle, delay = 0.01, speed = 10):
    step = speed if target_angle > servo.angle else -speed
    for angle in range(int(servo.angle), target_angle, step):
        servo.angle = angle
        time.sleep(delay)
def action1():
    move(servo15, 115, delay=0.01, speed=4)
    move(servo12, 40, delay=0.05, speed=1)
    move(servo12, 180, delay=0.01, speed=15)
def action2():
    count = 0
    while count < 3:
        move(servo15, 115, delay=0.01, speed=4)
        move(servo12, 125, delay=0.01, speed=15)
        move(servo12, 0, delay=0.01, speed=15)
        time.sleep(0.01)
        count += 1
def action3():
    move(servo15, 115, delay=0.01, speed=10)
    move(servo12, 125, delay=0.01, speed=10)
    move(servo12, 0, delay=0.01, speed=10)

#main code here
while True:
    if switch.value:
        random.choice(action1, action2, action3)
        time.sleep (0.5)
        while switch.value:
            move(servo12, 0, delay=0.01, speed=10)
            servo12.angle = 180
            time.sleep(0.5)

            move(servo15, 0, delay=0.01, speed=10)
            time.sleep(0.2)
            move(servo15, 15, delay=0.01, speed=10)
            time.sleep(0.2)
        else:
            move(servo12, 0, delay=0.02)
            servo15.angle = 15
