class Time:
    def __init__(self, time="00:00"):
        hr, min = time.split(":")
        self.hrs = int(hr)
        self.min1 = int(min)

# obj1+obj2
    def __add__(self, other):
        tn = Time()
        tn.hrs = self.hrs + other.hrs
        tn.min1 = self.min1 + other.min1
        if tn.min1 >= 60:
            tn.hrs += 1
            tn.min1 -= 60
        return tn

    def __sub__(self, other):
        tn = Time()
        tn.hrs = self.hrs - other.hrs
        tn.min1 = self.min1 - other.min1
        if tn.min1 < 0:
            tn.hrs -= 1
            tn.min1 += 60
        return tn

    def __mul__(self, multiplier):
        tn = Time()
        tn.hrs = self.hrs * multiplier
        tn.min1 = self.min1 * multiplier
        tn.hrs += tn.min1 // 60
        tn.min1 = tn.min1 % 60
        return tn

    def get_time(self):
        return self.hrs, self.min1


# assume minutes is never >60
time = input("Enter time1 HH:MM")
t1 = Time(time)
time = input("Enter time2 HH:MM")
t2 = Time(time)

t3 = t1 + t2
hrs, min1 = t3.get_time()
print(f"Sum of times: {hrs}hours and {min1}minutes")

# Assumes that t1 time is greater than t2
t3 = t1 - t2
hrs, min1 = t3.get_time()
print(f"Difference in times: {hrs}hours and {min1}minutes")

x = int(input("Enter multiplier"))
t3 = t2 * x
hrs, min1 = t3.get_time()
print(f"{x} times {t2.get_time()} is: {hrs}hours and {min1}minutes")
