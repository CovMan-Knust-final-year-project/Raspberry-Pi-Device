import requests
from Urls import *

class AttendanceManager:
    def __init__(self, person_id):
        self.person_id = person_id
        self.url = Urls().markAttendance()

    def MarkAttendance(self):
        print("Person id = " + self.person_id)

        #save attendance to database using the api
        headers = {}
        payload={'person_id': self.person_id, 'org_id' : 24, 'venue': 2}
        files = []

        response = requests.request("POST", self.url, headers=headers,
                                    data=payload, files=files)
        if(response.status_code == 201):
            print("failed")
            return "APIError: status={}".format(resp.status_code)
        results = response.json()
        if(results['status'] == "success"):
            print("Attendance marked successfully")
            #Scan temperature here
            #scanTemperature(results['user_id'])
            return
        print(results['message'])

