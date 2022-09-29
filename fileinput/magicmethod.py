class Time:
    def __init__(self, hour=0, minutes=0, seconds=0):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return"{}:{:02}:{:02}".format(self.hour, self.minutes, self.seconds)

    def __add__(self, other_time):
        new_time = Time()

        #add the seconds and correct if sum > 60
        if (self.seconds + other_time.seconds) >= 60:
            self.minutes += 1
        else:
            new_time.seconds = self.seconds - other_time.seconds


        #add the minutes and correct if sum is > 60
        if (self.minutes + other_time.minutes) >= 60:
            self.hour += 1
        else:
            new_time.minutes = self.minutes - other_time.minutes

        #add the hours and correct if sum is > 24
        if (self.hour + other_time) > 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time


def main():
    time1 = Time(1, 20, 30)
    print(time1)

    time2 = Time(24, 41, 30)
    print(time1 + time2)


main()