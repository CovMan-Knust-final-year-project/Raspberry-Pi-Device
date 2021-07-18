import requests
from Urls import *
from AttendanceManager import *

class FetchUserIdFromDatabase:
    def __init__(self, name):
        self.person_name = name
        self.url = Urls().fetchUserUsingName()

    def fetchPersonId(self):
        print("Person name = " + self.person_name)

        try:
            #fetch user from database using the api
            headers = {}
            payload={'name': self.person_name}
            files = []

            response = requests.request("POST", self.url, headers=headers,
                                        data=payload, files=files)
            if(response.status_code == 201):
                print("failed")
                return "APIError: status={}".format(resp.status_code)
            results = response.json()
            if(results['status'] == "success"):
                #print("the user id = " + results['user_id'])
                #mark the attendance here
                AttendanceManager(results['user_id'], self.person_name).MarkAttendance()
                return
            print(results['message'])
            
        except ValueError:
            print("Something went wrong with API")

