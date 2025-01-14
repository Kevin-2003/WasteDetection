#Camera Integration
import os
import time
from random_string import RandomName as randname
from resnet_ml_model import ImageModel as img
from servo import ServoMotor
from ultrasonic import Ultra

myUltra = Ultra()
myServo = ServoMotor()
myServo.set_angle(45)
time.sleep(1)
dist = Ultra.read_sensor()
perc = ((12-dist)/12)*100
if (perc <= 80):
    name = randname.randomStringGenerator()
    os.system(f"libcamera-jpeg -o /home/pi/Documents/WasteManagement/Garbage_Images/{name}.jpg -t 5000 --width 684 --height 684")
    time.sleep(1)
    predicted = img.imageClassification(name)
    print(predicted)
    if predicted == 'plastic' or predicted == 'glass' or predicted == 'metal':
        myServo.set_angle(0)
        time.sleep(5)
        myServo.set_angle(45)
        time.sleep(3)
    else:
        myServo.set_angle(120)
        time.sleep(5)
        myServo.set_angle(45)
        time.sleep(2)
else:
    print("Garbage bin capacity almost full, please empty the contents")
