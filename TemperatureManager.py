import requests
from Urls import *
from Variables import *
from smbus2 import SMBus
from mlx90614 import MLX90614

import time
from gpiozero import Buzzer


## buzzer initialization starts here
buzzer = Buzzer(5)
## buzzer initialization ends here

class TemperatureManager:
    def __init__(self, person_id, person_name):
        self.person_id = person_id
        self.person_name = person_name
        self.variables = Variables()
        self.url = Urls().saveTemperature()

    def scanTemperature(self):
        #acquire the temperature from the sensor
        try:
            bus = SMBus(1)
            sensor = MLX90614(bus, address=0x5A)
            print("Ambient temperature: {}".format(sensor.get_ambient()))
            print("Object temperature of {}: {}".format(self.person_name, sensor.get_object_1()))

            #save the acquired sensor value
            #rounding value to 2 decimal places
            self.saveTemperature(round(sensor.get_object_1(),2))
            bus.close()
            
        except OSError as error:
            print(error)
            print("Check temperature sensor pins")
        
    def saveTemperature(self, temp):
        try:
            #save temperature to database using the api
            headers = {}
            payload={'person_id': self.person_id, 'org_id' : self.variables.org_id(), 'venue': self.variables.mount_point_id(), 'temp': temp}
            files = []

            response = requests.request("POST", self.url, headers=headers,
                                        data=payload, files=files)
            if(response.status_code == 201):
                print("failed")
                return "APIError: status={}".format(resp.status_code)
            #time.sleep(5)
            results = response.json()
            if(results['status'] == "success"):
                print("Temperature for {} saved successfully".format(self.person_name))
                ## buzz here
                buzzer.on()
                time.sleep(1)
                buzzer.off()
                time.sleep(1)
                #dispense sanitizer here
                return
            print(results['message'])
            
        except ValueError:
            print("Something went wrong with API")

#TemperatureManager(6, "Jesse Anim").scanTemperature()
