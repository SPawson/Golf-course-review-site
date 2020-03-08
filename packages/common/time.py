from datetime import datetime

class Time(object):
#Converts unix time to readable date
    @staticmethod
    def return_time(unix_time):
        timestamp = float(unix_time)
        conversion = datetime.fromtimestamp(timestamp)
        time = conversion.strftime("%d %B %Y")

        return time

