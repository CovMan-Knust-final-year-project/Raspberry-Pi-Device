# Raspberry-Pi-Device

# Description
This project uses [Tensorflow] and [openCV] with [python] and [PHP] for the apis.
The raspberry pi 3B was used for the project. It turns out that Tensorflow runs extremely slow on this particular version of raspberry pi
especially for the facial recognition and nose mask aspect.

So the [facial_section] is run on the host machine. And a server listens for data from the host machine to start working the PI processes.
Processes include
[Start server for recieving name from host machine]
[Use name to find id of person]
[Use id to mark attendance]
[Scan and save temperature]
[Dispense sanitizer]
[Send Sms]


## installation
I. (optional) Install Anaconda

(optional)
II. Activate conda virtual env
```
conda activate
```

1. install Tensorflow
```
pip3 install tensorflow --user
```
 
2. install OpenCV
```
pip3 install opencv-python
```

3. check tensorflow, and display tensorflow version
```
import tensorflow as tf
tf.__version__

check OpenCV, and display OpenCV version
import cv2
cv2.__version__
```

4. install face-recognition
```
pip3 install face-recognition
```

5. install imutils
```
pip3 install imutils
```

6. follow instructions in facial_section/README.md to set up the facial recognition
I. add images to dataset folder if you need to identify more persons
II. train dataset using train_model.py after adding the images

## running
navigate to [facial_section]

run ```facial_req.py``` on host machine

run ```main.py``` in Pi device




