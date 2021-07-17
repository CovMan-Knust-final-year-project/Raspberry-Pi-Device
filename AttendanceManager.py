import requests
from Urls import *
from Variables import *
from TemperatureManager import *


class AttendanceManager:
    def __init__(self, person_id, person_name):
        self.person_id = person_id
        self.person_name = person_name
        self.variables = Variables()
        self.url = Urls().markAttendance()

    def MarkAttendance(self):
        print("Person id = " + self.person_id)

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
            TemperatureManager(self.person_id, self.person_name).scanTemperature()
            return
        print(results['message'])

