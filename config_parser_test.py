import configparser

config = configparser.ConfigParser()
config.read("student.ini")
print(config["student"]["Rollno"])
