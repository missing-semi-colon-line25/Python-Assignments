class Student:

    def __init__(self, reg_no=0, name=''):
        self.reg_no = reg_no
        self.name = name

    def set_reg_no(self, reg_no):
        self.reg_no = reg_no

    def set_name(self, name):
        self.name = name

    def get_reg_no(self):
        return self.reg_no

    def get_name(self):
        return self.name


class Exam:

    def __init__(self, ex_no=1, pattern='', semester=''):
        self.ex_no = ex_no
        self.pattern = pattern
        self.semester = semester

    def set_data(self, ex_no=1, pattern='', semester=''):
        self.ex_no = ex_no
        self.pattern = pattern
        self.semester = semester

    def getdata(self):
        return self.ex_no, self.pattern, self.semester


class Result(Student, Exam):
    def __init__(self, ex_no, pattern, semester, reg_no, name):
        super().__init__(reg_no, name)
        Exam.__init__(self, ex_no, pattern, semester)
        self.phy = 0
        self.math = 0
        self.chem = 0

    def set_marks(self, phy, math, chem):
        self.phy = phy
        self.math = math
        self.chem = chem

    def call_result_grade(self):
        per = ((self.phy + self.math + self.chem) / 3) * 100
        if per < 40:
            return "F"
        elif per < 50:
            return "E"
        elif per < 60:
            return "D"
        elif per < 70:
            return "C"
        elif per < 80:
            return "B"
        elif per <= 100:
            return "A"
        else:
            return "Invalid percentage"


def main():
    while 1:
        choice = input("MENU: \n1.")
