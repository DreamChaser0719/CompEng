import RPi.GPIO as GPIO
import time

IN1 = 23 # motor A
IN2 = 24
IN3 = 27 # motor B
IN4 = 17

GPIO.setmode(GPIO.BCM)
for pin in [IN1, IN2, IN3, IN4]:
        GPIO.setup(pin, GPIO.OUT)

def motor_a(direction):
        GPIO.output(IN1, direction == "forward")
        GPIO.output(IN2, direction == "reverse")

def motor_b(direction):
        GPIO.output(IN3, direction == "forward")
        GPIO.output(IN4, direction == "reverse")
       

def stop():
        for pin in [IN1, IN2, IN3, IN4]:
                GPIO.output(pin, GPIO.LOW)

try:
        print("Both Forward 2s")
        motor_a("forward")
        motor_b("forward")
        time.sleep(2)

        print("Stop 0.5s")
        stop()
        time.sleep(0.5)

        print("Both reverse 2s")
        motor_a("reverse")
        motor_b("reverse")
        time.sleep(2)
        stop()
        time.sleep(0.5)        

print("Reverse 2s")
        motor_a("forward")
        motor_b("reverse")
        time.sleep(2)

        print("Stop")
        stop()

finally:
        GPIO.cleanup()
        print("Doner.")