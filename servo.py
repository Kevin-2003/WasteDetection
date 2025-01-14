from gpiozero import AngularServo
from time import sleep
class ServoMotor:
    def __init__(self, pin=14):
        self.servo = AngularServo(
            pin,
            min_angle=0,
            max_angle=180,
            min_pulse_width=0.5/1000,
            max_pulse_width=2.5/1000
        )
        
    def set_angle(self, angle):
        self.servo.angle = angle
