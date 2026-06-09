import RPi.GPIO as GPIO
import time

SENSOR = 22
LED    = 16

EN1 = 12
IN1 = 23
IN2 = 24
EN2 = 13
IN3 = 27
IN4 = 17
BUTTON_PIN = 25

Robot_State = False

THRESHOLD = 500   # replace with your calibrated value
SPEED = 60        # 0–100



GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.HIGH)
GPIO.setup(BUTTON_PIN, GPIO.IN)

for pin in [IN1, IN2, IN3, IN4, EN1, EN2]:
    GPIO.setup(pin, GPIO.OUT)

pwm_a = GPIO.PWM(EN1, 100)
pwm_b = GPIO.PWM(EN2, 100)
pwm_a.start(SPEED)
pwm_b.start(SPEED)

def RobotState(bool):
    print("yes")

def rc_time():
    GPIO.setup(SENSOR, GPIO.OUT)
    GPIO.output(SENSOR, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(SENSOR, GPIO.IN)
    count = 0
    while GPIO.input(SENSOR) == GPIO.LOW:
        count += 1
    return count

def forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def reverse():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

try:
    while True:
        reading = rc_time()
        print(reading)
        if reading > THRESHOLD:
            reverse()
        else:
            forward()
finally:
    pwm_a.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)
    pwm_a.stop()
    pwm_b.stop()
    del pwm_a, pwm_b
    GPIO.output(LED, GPIO.LOW)
    GPIO.cleanup()
    print("Done.")