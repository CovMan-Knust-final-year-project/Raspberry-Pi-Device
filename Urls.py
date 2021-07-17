class Urls:
    def __init__(self):
        self.initial = "http://192.168.43.19/CovMan/Iot/"

    def fetchUserUsingName(self):
        return self.initial + "fetch_user_from_name.php"

    def markAttendance(self):
        return self.initial + "markAttendance.php"

    def saveTemperature(self):
        return self.initial + "saveTemperature.php"
