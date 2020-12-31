# Project: RARroad

## Project Description
RARroad is a computer vision based system that will assist the driver as road awareness is added in the rover using deep learning algorithms implemented on Raspberry Pi.

The system consists of two stages. The first stage focuses on “Traffic signboard detection” and the second stage focuses on “Traffic sign classification and recognition." Raspberry pi camera module will take Video input from the surroundings and whenever a traffic sign appears, the system will:
1) Generate alerts to notify the driver through an Android application. 
2) Change the rover behavior accordingly using Arduino Uno.

## YOLOv3
With YOLO, a single CNN simultaneously predicts multiple bounding boxes and class probabilities for those boxes. YOLO trains on full images and directly optimizes detection performance. This model has a number of benefits over other object detection methods: YOLO is extremely fastand accurate.
A Pre-trained model, YOLOv3, is used for the purpose of traffic sign detection and recognition. This is done for the reason of efficiency, as the traffic sign recognition system has to be implemented on a rover as a proof of concept. The algorithm will be able to give us maximum accurate results under minimum time. The YOLOv3 model is pretrained on COCO dataset, and weights are set according to it. Just using this platform and pre-trained weights, we retrained the model according to our need and our selected and prepared dataset. The model weights are downloaded from the darknet yolo website https://pjreddie.com/darknet/yolo/. 

## TrafficSign_Dataset
The dataset is taken from INI Benchmark Website i.e. https://benchmark.ini.rub.de/?section=gtsdb&subsection=dataset. From here the GTSDB (The German Traffic Sign Detection Bencmark Dataset) was selected and prepared according to the need of the project.
The project dataset includes selective traffic signs including speed limit signs, yield signs, warning signs, etc. The traffic sign detection and recognition will be done using the German Traffic Sign Detection Benchmark (GTSDB) dataset. Thus, two extensive functionalities (detection and recognition) will be implemented to provide road safety.
Dataset is prepared according to our own requirement and scope. There are 4 preselected signs that are:
1. Stop sign
2. Speed limit Sign 30
3. Speed limit Sign 50
4. Yield sign

Image folder: Contains all the images of the dataset  
Label folder: Contains all the text files of images    
Classes.txt: It contains five classes of traffic signs which are stop sign, yield sign, speed limit 30, speed limit 50, others  
train.txt: It contains the paths and bounded boxes for the image files that are used for training the model.  
text.txt: It contains the paths and bounded boxes for the image files that are used for testing the model.  
TrafficSignDetection: This python Notebook contains the code for training and testing the model.  

## Manual  
Change the runtime type to GPU in google colab.  
After cloning the qqwweee respository https://github.com/qqwweee/keras-yolo3, change the following paths to train and test the model.  
train.py:  
Change the path of model weights in line 33  
Change the path of classes.txt in line 19  
Change the path of yolo_anchors.txt in line 20  
Change the batch size to 8 in line 76  

yolo.py:  
Change the path of final model in line 23  
Change the path of yolo_anchors.txt in line 24  
Change the path of classes.txt in line 25  

