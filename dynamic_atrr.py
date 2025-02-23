from types import MethodType


class Student:
    pass


s1 = Student()
setattr(s1, "reg_no", 101)
setattr(s1, "name", "Ayush")
# s1.__setattr__("reg_no", 101)
# s1.__setattr__("name", "Ayush")

print("dynamic attributes set")


def set_data(self, reg_no, name):
    self.reg_no = reg_no
    self.name = name


def get_data(self):
    return f"Registration number:{self.reg_no}, Name :{self.name}"


s1.set_data = MethodType(set_data, s1)
s1.get_data = MethodType(get_data, s1)
print("Dynamic attributes before method calls: \n", get_data(s1))
reg_no = int(input("Enter registration number:"))
name = input("Enter name:")
print("After dynamic methods added and called:")
set_data(s1, reg_no, name)
print(get_data(s1))
