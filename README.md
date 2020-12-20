# TrafficSign_Dataset

Image folder: Contains all the images of the dataset  
Label folder: Contains all the text files of images    
Classes.txt: It contains five classes of traffic signs which are stop sign, yield sign, speed limit 30, speed limit 50, others  
train.txt: It contains the paths and bounded boxes for the image files that are used for training the model.  
text.txt: It contains the paths and bounded boxes for the image files that are used for testing the model.  
TrafficSignDetection: This python Notebook contains the code for training and testing the model.  
  
## Manual  
After cloning the qqwweee repository, change the following paths to train and test your model:  
train.py:  
Change the path of weight file according to your path to weight file in line 33  
Change the path of classes.txt in line 19  
Change the path of yolo_anchors.txt in line 20  
  
yolo.py:  
Change the path of model in line 23 to your trained model  
Change the path of yolo_anchors.txt in line 24  
Change the path of classes.txt in line 25
