import requests
from Urls import *
from Variables import *
from TemperatureManager import *

import RPi.GPIO as GPIO
import time

from gpiozero import Buzzer

### initializations for the ultrasonic sensor
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

### initializations for the ultrasonic sensor ends here

class AttendanceManager:
    def __init__(self, person_id, person_name):
        self.person_id = person_id
        self.person_name = person_name
        self.variables = Variables()
        self.url = Urls().markAttendance()

    def distance(self):
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)
     
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
     
        StartTime = time.time()
        StopTime = time.time()
     
        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
     
        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
     
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
     
        return distance

    def MarkAttendance(self):
        print("Person id = " + self.person_id)

        try:
            #save attendance to database using the api
            headers = {}
            payload={'person_id': self.person_id, 'org_id' : self.variables.org_id(), 'venue': self.variables.mount_point_id()}
            files = []

            response = requests.request("POST", self.url, headers=headers,
                                        data=payload, files=files)
            if(response.status_code == 201):
                print("failed")
                return "APIError: status={}".format(resp.status_code)
            results = response.json()
            if(results['status'] == "success"):
                print("Attendance for {} marked successfully".format(self.person_name))
                
                #Scan temperature here
                #continously check if the persons hand is within a 10cm or less

                while True:
                    dist = self.distance()
                    print ("Measured Distance = %.1f cm" % dist)
                    time.sleep(1)
                    if(dist <= 10):
                        TemperatureManager(self.person_id, self.person_name).scanTemperature()
                        GPIO.cleanup()
                        return
                return
            print(results['message'])

        except ValueError:
            print("Something went wrong with API")

