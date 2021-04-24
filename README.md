# Project: RARroad

## Project Description
RARroad is a computer vision based system that will assist the driver as road awareness is added in the rover using deep learning algorithms implemented on Raspberry Pi.

The system consists of two stages. The first stage focuses on “Traffic signboard detection” and the second stage focuses on “Traffic sign classification and recognition." Raspberry pi camera module will take Video input from the surroundings and whenever a traffic sign appears, the system will:
1) Predict traffic signs present in a real time video.
2) Generate alerts to notify the driver through an Android application.



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

## Manual to Training weights
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

## Traffic sign Detection and Recognition Model
After training of the specialized weights for our dataset, the weights are then loaded and converted into the model using yolov3 utilitis. The model is according to the classes present and is now ready to make new predictions. This all is implemented in FYPII.ipnyb's class YOLO(). YOLO() class in this file has been *referenced* from https://github.com/qqwweee/keras-yolo3 repository. On creating an object of this class, all the functionalities can be accessed and signs can be predicted for input image or videos via detect_image() function.  
The model produces the following output:
1. Predicted traffic signs names
2. Time taken to predict the sign
3. Confidence value of sign
4. Bounded boxes of the sign

## RARRoad Android Application
A part of this project was to create an android application that will help us in alerting the drivers about the incoming traffic signs so they can take action. The android application is present in the zip folder *RARroad_FINAL* and was made using android studio. In this application, JAVA is used as a back-end language and XML is used a front-end language. It is a simple application providing the user with an easy to use interface so anyone can use it anywhere. The application provides additional information and facts related to Traffic signs and Road safety. On clicking the start directing button present on the home screen, the driver will be able to get live feed from the model implemented on Raspberry pi 3.  
A demonstration of the android application can be watched in the *Final Model Application_4.mp4* video which is present in *DemoVideos* folder. 
### Connection of Deep learning Model with Mobile Application:            
   The connection between rpi 3 and android appication is made through socket programming (UDP connection). In this connection, RPI model is acting as a server and the android application is working as a client which is requesting for model predictions on the real time video being captured via rpi camera.

## Model Deployment on Rasberry Pi
Before the deployment of model on raspberry pi 3, some necessary installations are required. These installation are listed in the file *Rpi Installations.txt*. After installations, SCP Protocol from MobaXterm was used to transfer files from laptop to raspberry pi. Due to low processing speed of raspberry pi 3, the model output was bit lagging as compared to the real time input video. This issue was solved by minimizing the work load on raspberry pi through limiting the connections formed between Rpi and Android application. Frames were also dropped from the video feed to avoid the useless frames from burdening the Rpi. 
### Project Demo  
All the progress of the project from start to end can be watched in the demo videos present in DemoVideos folder.

