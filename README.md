# Project: RARroad

# Project Description
RARroad is a computer vision based system that will assist the driver as road awareness is added in the rover using deep learning algorithms implemented on Raspberry Pi.

The system consists of two stages. The first stage focuses on “Traffic signboard detection” and the second stage focuses on “Traffic sign classification and recognition." Raspberry pi camera module will take Video input from the surroundings and whenever a traffic sign appears, the system will:
1) Generate alerts to notify the driver through an Android application. 
2) Change the rover behavior accordingly using Arduino Uno.



# TrafficSign_Dataset
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
