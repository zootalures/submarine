#!/usr/bin/python3

from servo import Servo

class Motion:
    def __init__(self, servos : list[Servo]):
        self.servos = servos
        self.magnitude = 0
        self.angle = 0
        self.direction =0

    def set_direction(self,magnitude,angle,direction):
        self.magnitude = magnitude
        self.angle = angle
        self.direction = direction

    def  set_servos(self, rotor_angle):
