import random
import time
import board
import pwmio
import digitalio
from adafruit_motor import servo

buzzer = pwmio.PWMOut(board.GP22, variable_frequency = True)
pwm_servo14 = pwmio.PWMOut(board.GP14, frequency=50)
servo14 = servo.Servo(pwm_servo14)
pwm_servo12= pwmio.PWMOut(board.GP12, frequency=50)
servo12 = servo.Servo(pwm_servo12)
pwm_servo15 = pwmio.PWMOut(board.GP15, frequency=50)
servo15 = servo.Servo(pwm_servo15)
switch = digitalio.DigitalInOut(board.GP0)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN

servo12.angle = 0
servo15.angle = 15
servo14.angle = 100

NOTE_B0  = 31
NOTE_C1  = 33
NOTE_CS1 = 35
NOTE_D1  = 37
NOTE_DS1 = 39
NOTE_E1  = 41
NOTE_F1  = 44
NOTE_FS1 = 46
NOTE_G1  = 49
NOTE_GS1 = 52
NOTE_A1  = 55
NOTE_AS1 = 58
NOTE_B1  = 62
NOTE_C2  = 65
NOTE_CS2 = 69
NOTE_D2  = 73
NOTE_DS2 = 78
NOTE_E2  = 82
NOTE_F2  = 87
NOTE_FS2 = 93
NOTE_G2  = 98
NOTE_GS2 = 104
NOTE_A2  = 110
NOTE_AS2 = 117
NOTE_B2  = 123
NOTE_C3  = 131
NOTE_CS3 = 139
NOTE_D3  = 147
NOTE_DS3 = 156
NOTE_E3  = 165
NOTE_F3  = 175
NOTE_FS3 = 185
NOTE_G3  = 196
NOTE_GS3 = 208
NOTE_A3  = 220
NOTE_AS3 = 233
NOTE_B3  = 247
NOTE_C4  = 262
NOTE_CS4 = 277
NOTE_D4  = 294
NOTE_DS4 = 311
NOTE_E4  = 330
NOTE_F4  = 349
NOTE_FS4 = 370
NOTE_G4  = 392
NOTE_GS4 = 415
NOTE_A4  = 440
NOTE_AS4 = 466
NOTE_B4  = 494
NOTE_C5  = 523
NOTE_CS5 = 554
NOTE_D5  = 587
NOTE_DS5 = 622
NOTE_E5  = 659
NOTE_F5  = 698
NOTE_FS5 = 740
NOTE_G5  = 784
NOTE_GS5 = 831
NOTE_A5  = 880
NOTE_AS5 = 932
NOTE_B5  = 988
NOTE_C6  = 1047
NOTE_CS6 = 1109
NOTE_D6  = 1175
NOTE_DS6 = 1245
NOTE_E6  = 1319
NOTE_F6  = 1397
NOTE_FS6 = 1480
NOTE_G6  = 1568
NOTE_GS6 = 1661
NOTE_A6  = 1760
NOTE_AS6 = 1865
NOTE_B6  = 1976
NOTE_C7  = 2093
NOTE_CS7 = 2217
NOTE_D7  = 2349
NOTE_DS7 = 2489
NOTE_E7  = 2637
NOTE_F7  = 2794
NOTE_FS7 = 2960
NOTE_G7  = 3136
NOTE_GS7 = 3322
NOTE_A7  = 3520
NOTE_AS7 = 3729
NOTE_B7  = 3951
NOTE_C8  = 4186
NOTE_CS8 = 4435
NOTE_D8  = 4699
NOTE_DS8 = 4978


melody = [
    NOTE_E3, NOTE_C3, 0, NOTE_B3, 0, NOTE_D7, NOTE_F7, 0, NOTE_G7, 0, 0, 0, NOTE_E7, 0, 0, 0,
    NOTE_C7, 0, 0, NOTE_B6, 0, 0, NOTE_E6, 0, 0, NOTE_A6, 0, NOTE_B6, 0, NOTE_AS6, NOTE_A6, 0,
    NOTE_G6, NOTE_E7, NOTE_G7, NOTE_A7, 0, NOTE_F7, NOTE_G7, 0, NOTE_E7, 0, NOTE_C7, NOTE_D7, NOTE_B6, 0, 0,
    NOTE_C7, 0, 0, NOTE_G6, 0, 0, NOTE_E6, 0, 0, NOTE_A6, 0, NOTE_B6, 0, NOTE_AS6, NOTE_A6, 0,
    NOTE_G6, NOTE_E7, NOTE_G7, NOTE_A7, 0, NOTE_F7, NOTE_G7, 0, NOTE_E7, 0, NOTE_C7, NOTE_D7, NOTE_B6, 0, 0
]

tempo = [
    12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
    12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
    9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
    12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
    9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12
]

def move(servo, target_angle, delay = 0.01, speed = 10):
    step = speed if target_angle > servo.angle else -speed
    for angle in range(int(servo.angle), target_angle, step):
        servo.angle = angle
        time.sleep(delay)

def play_melody(melody, tempo):
    base_tempo = 0.8  # Base duration for a single beat (adjust as needed)
    for i in range(len(melody)):
        note_duration = base_tempo / tempo[i]
        if melody[i] != 0:
            buzzer.frequency = melody[i]
            buzzer.duty_cycle = 65536 // 2  # 50% volume
            time.sleep(note_duration)
        else:
            time.sleep(note_duration)  # Rest period for note value 0
        buzzer.duty_cycle = 0  # Silence between notes
        time.sleep(0.05)

# multiple actions
def action1():
    play_melody(melody, tempo)
    move(servo15, 115, delay=0.01, speed=4)
    move(servo12, 40, delay=0.05, speed=1)
    move(servo12, 180, delay=0.01, speed=15)
def action2():
    play_melody(melody, tempo)
    move(servo15, 115, delay=0.01, speed=4)
    count = 0
    while count < 3:
        move(servo12, 125, delay=0.01, speed=15)
        move(servo12, 0, delay=0.01, speed=15)
        time.sleep(0.01)
        count += 1
    move(servo12, 40, delay=0.01, speed=5)
    move(servo12, 180, delay=0.01, speed=10)
def action3():
    move(servo15, 115, delay=0.01, speed=10)
    move(servo12, 180, delay=0.01, speed=10)
def action4():
    move(servo)

#random action list
action_list = [action1, action2, action3]
#main code here
while True:
    if switch.value:
        play_melody(melody, tempo)
        random.choice(action_list)()
        move(servo14, 100, delay=0.01, speed=12)
        time.sleep (0.01)
        while switch.value:
            move(servo12, 0, delay=0.01, speed=10)
            servo12.angle = 180
            time.sleep(0.5)

            move(servo15, 0, delay=0.01, speed=10)
            time.sleep(0.2)
            move(servo15, 15, delay=0.01, speed=10)
            time.sleep(0.2)
    if switch.value == False:
        move(servo12, 0, delay=0.01, speed=10)
        move(servo15, 15, delay=0.01, speed=10)
        servo15.angle = 15