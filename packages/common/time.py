from datetime import datetime

class Time(object):

    @staticmethod
    def return_time(unix_time):
        timestamp = float(unix_time)
        conversion = datetime.fromtimestamp(timestamp)

        time = conversion.strftime("%d-%m-%Y")

        return time

