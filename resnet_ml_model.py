import numpy as np
import tensorflow as tf
import tflite_runtime.interpreter as tflite
import cv2

class ImageModel:
    def imageClassification(name):
        class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic']
        img_width,img_height=512,512
        interpreter = tflite.Interpreter(model_path="/home/pi/Documents/WasteManagement/Trashnet_Resnet/trash_model_512.tflite")
        interpreter.allocate_tensors()
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        
        image=cv2.imread(str(f"/home/pi/Documents/WasteManagement/Garbage_Images/{name}.jpg"))
        image_resized= cv2.resize(image, (img_height,img_width))
        image_np=np.expand_dims(image_resized,axis=0)
        image_np = np.array(image_np, dtype=np.float32)
        
        interpreter.set_tensor(input_details[0]['index'], image_np)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])
        output_class=class_names[np.argmax(output_data)]
        return output_class
