# Raspberry-Pi-Device

# Description
The raspberry pi 3B was used for the project. It turns out that Tensorflow runs extremely slow on this particular version of raspberry pi
especially for the facial recognition and nose mask aspect.

So the facial_section is run on the host machine. And a server listens for data from the host machine to start working the PI.

#installation
*optional* Install Anaconda

*optional*
Activate conda virtual env

conda activate

install Tensorflow
pip install tensorflow --user
 
install OpenCV
pip install opencv-python

check tensorflow, and display tensorflow version
import tensorflow as tf
tf.__version__

check OpenCV, and display OpenCV version
import cv2
cv2.__version__

install face-recognition
pip3 install face-recognition

install imutils
pip install imutils

follow instructions in facial_section/README.md to set up the facial recognition

# running
navigate to facial_section

run facial_req.py on host machine

navigate back to root directory
run main.py




