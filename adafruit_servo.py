from adafruit_servokit import ServoKit
from servo import Servo
from adafruit_motor import  servo


class AdafruitServo(Servo) :

    def __init__(self, servo : servo.Servo):
        self.servo = servo
        self.servo.set_pulse_width_range(500, 2500)

    def set_angle(self, angle):
        self.servo.angle = angle
