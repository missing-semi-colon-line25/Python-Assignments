class Date:
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, date=1, month=1, year=2000):
        self.date = date
        self.month = month
        self.year = year

    def __add__(self, other):
        if isinstance(other, int):
            self.date += other
            self.normalize()

    def normalize(self):
        while True:
            if self.month == 2 and self.is_leap_year(self.year):
                days_in_month = 29
            else:
                days_in_month = Date.months[self.month]

            if self.date > days_in_month:
                self.date -= days_in_month
                self.month += 1
                if self.month > 12:
                    self.month = 1
                    self.year += 1
            else:
                break

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def get_date(self):
        return f"{self.date} / {self.month} / {self.year}"


# d1 = Date(2, 5, 2014)
# d2 = Date(28, 2, 2024)
# d3 = Date(31, 12, 2014)
# d1 + 1
# d2 + 1
# d3 + 1
# print(d1.get_date())
# print(d2.get_date())
# print(d3.get_date())
date_str = input("Enter date: ")
d, m, y = date_str.split("/")
d = int(d)
m = int(m)
y = int(y)
d1 = Date(d, m, y)
d1 + 1

print("Tomorrow's Date:  " + d1.get_date())
