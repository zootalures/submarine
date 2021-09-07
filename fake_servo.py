from servo import Servo


class FakeServo(Servo):

    def __init__(self):
        self.angle = 0

    def set_angle(self, angle):
        self.angle = angle

