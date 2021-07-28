import tensorflow
from tensorflow.python import keras
import numpy as np # linear algebra
import cv2
import socket
import json
import threading
from io import StringIO
from _thread import *     
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import time
from picamera.array import PiRGBArray
from picamera import PiCamera

# -*- coding: utf-8 -*-

# REFERENCE: qqwweee github repository
"""
Class definition of YOLO_v3 style detection model on image and video
"""
import numpy as np
from keras import backend as K
from keras.models import load_model
from keras.layers import Input
from PIL import Image
from yolo3.model import yolo_eval, yolo_body, tiny_yolo_body
from yolo3.utils import letterbox_image
import os
from keras.utils import multi_gpu_model

class YOLO(object):
    _defaults = {
        "model_path": '/home/pi/Desktop/RARModel/trained_weights_final.h5',
        "anchors_path": '/home/pi/Desktop/RARModel/yolo3/yolo_anchors.txt',
        "classes_path": '/home/pi/Desktop/RARModel/classes.txt',
        "score" : 0.3,
        "iou" : 0.45,
        "model_image_size" : (416, 416),
        "gpu_num" : 1,
    }

    def get_defaults(cls, n):
        if n in cls._defaults:
            return cls._defaults[n]
        else:
            return "Unrecognized attribute name '" + n + "'"

    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults) # set up default values
        self.__dict__.update(kwargs) # and update with user overrides
        self.class_names = self._get_class()
        self.anchors = self._get_anchors()
        self.sess = K.get_session()
        self.boxes, self.scores, self.classes = self.generate()

    #return the names of classes
    def _get_class(self):
        classes_path = os.path.expanduser(self.classes_path)
        with open(classes_path) as f:
            class_names = f.readlines()
        class_names = [c.strip() for c in class_names]
        return class_names

    def _get_anchors(self):
        anchors_path = os.path.expanduser(self.anchors_path)
        with open(anchors_path) as f:
            anchors = f.readline()
        anchors = [float(x) for x in anchors.split(',')]
        return np.array(anchors).reshape(-1, 2)

    def generate(self):
        model_path = os.path.expanduser(self.model_path)
        assert model_path.endswith('.h5'), 'Keras model or weights must be a .h5 file.'

        # Load model, or construct model and load weights.
        num_anchors = len(self.anchors)
        num_classes = len(self.class_names)
        is_tiny_version = num_anchors==6 # default setting
       
        self.yolo_model = tiny_yolo_body(Input(shape=(None,None,3)), num_anchors//2, num_classes) \
            if is_tiny_version else yolo_body(Input(shape=(None,None,3)), num_anchors//3, num_classes)
        self.yolo_model.load_weights(self.model_path) # make sure model, anchors and classes match
       
        # Generate output tensor targets for filtered bounding boxes.
        self.input_image_shape = K.placeholder(shape=(2, ))
        if self.gpu_num>=2:
            self.yolo_model = multi_gpu_model(self.yolo_model, gpus=self.gpu_num)
        boxes, scores, classes = yolo_eval(self.yolo_model.output, self.anchors,
                len(self.class_names), self.input_image_shape,
                score_threshold=self.score, iou_threshold=self.iou)
        return boxes, scores, classes

    def detect_image(self):
        
        if self.model_image_size != (None, None):
            assert self.model_image_size[0]%32 == 0, 'Multiples of 32 required'
            assert self.model_image_size[1]%32 == 0, 'Multiples of 32 required'
            boxed_image = letterbox_image(image, tuple(reversed(self.model_image_size)))
        else:
            new_image_size = (image.width - (image.width % 32),
                              image.height - (image.height % 32))
            boxed_image = letterbox_image(image, new_image_size)
        image_data = np.array(boxed_image, dtype='float32')

        image_data /= 255.
        image_data = np.expand_dims(image_data, 0)  # Add batch dimension.

        out_boxes, out_scores, out_classes = self.sess.run(
            [self.boxes, self.scores, self.classes],
            feed_dict={
                self.yolo_model.input: image_data,
                self.input_image_shape: [image.size[1], image.size[0]],
                K.learning_phase(): 0
            })

        print('Found {} boxes for {}'.format(len(out_boxes), 'img'))
        
        thickness = (image.size[0] + image.size[1]) // 300
        for i, c in reversed(list(enumerate(out_classes))):
            predicted_class = self.class_names[c]
            box = out_boxes[i]
            score = out_scores[i]
            label = '{} {:.2f}'.format(predicted_class, score)
            print(label)            
        return out_classes
   
    """Threaded functions accepts the socket connection and sends 
    the predicted labels to the android application """
    def threaded(self,con):        
        print(class_labels)
        if len(class_labels) != 0:
            con.send(json.dumps({"label":int(class_labels[0])}).encode('utf-8'))
        con.close() 
            
    #closing the session of YOLO object
    def close_session(self):
        self.sess.close()


#************************** Making YOLO object ***********************#
yolo1 = YOLO()

port = 5000
global class_labels
#Create socket for connecting android application
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", port))
s.listen(5)   

# store the previous label
pre = -1

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# Taking real time input and using YOLO object to detect and recognize signs
while True:
    # allow the camera to warmup
    time.sleep(0.1)
    # grab an image from the camera
    camera.capture(rawCapture, format="bgr")
    #extract the camera
    frame = rawCapture.array
    cv2.imwrite("frame.jpg",frame)
    image=Image.open("frame.jpg")
    #Call YOLO class function to detect all the labels in the frame
    class_labels = yolo1.detect_image()
    print(class_labels)
    
    i = 0
    #drop some of the frames
    while(i<13):
        frame = video.read()
        i+=1
    #Now lets accept connections from devices and connect with them
    if(len(class_labels) == 0):
        continue
    elif (pre == int(class_labels[0])):
        continue
        
    print("Waiting for client connection") 
    conn, addr = s.accept()
    print("Connected to",conn,":",addr)
    start_new_thread(yolo1.threaded, (conn,))
    pre = int(class_labels[0])
    
cv2.destroyAllWindows()    
s.close()
#************************** Closing Session **************************#
yolo1.close_session()



