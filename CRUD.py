def validate_roll_number(roll_number):
    return roll_number.isdigit() and 1 <= int(roll_number) <= 100


def validate_mark(mark):
    return mark.isdigit() and 0 <= int(mark) <= 100


def validate_name(name):
    return name.isalpha()


def check_record_exists(student_dict, roll_number):
    return roll_number in student_dict


def create_student(student_dict):
    roll_number = input("Enter Roll Number (1-100): ")
    if not validate_roll_number(roll_number):
        print("Invalid roll number! Please enter a number between 1 and 100.")
        return

    if check_record_exists(student_dict, roll_number):
        print("Record for this roll number already exists!")
        return

    name = input("Enter Student Name: ")
    if not validate_name(name):
        print("Invalid name! Name cannot contain numbers.")
        return

    marks = []
    for subject in ['Physics', 'Chemistry', 'Math']:
        mark = input(f"Enter marks for {subject} (0-100): ")
        if not validate_mark(mark):
            print(f"Invalid mark for {subject}! Please enter a number between 0 and 100.")
            return
        marks.append(int(mark))

    student_dict[roll_number] = {'Name': name, 'Marks': marks}
    print("Student record created successfully!")


def view_student(student_dict):
    roll_number = input("Enter Roll Number to View: ")
    if not validate_roll_number(roll_number):
        print("Invalid roll number! Please enter a number between 1 and 100.")
        return

    if not check_record_exists(student_dict, roll_number):
        print("No record found for this roll number.")
        return

    print(f"Record for Roll Number {roll_number}: {student_dict[roll_number]}")


def update_student(student_dict):
    roll_number = input("Enter Roll Number to Update: ")
    if not validate_roll_number(roll_number):
        print("Invalid roll number! Please enter a number between 1 and 100.")
        return

    if not check_record_exists(student_dict, roll_number):
        print("No record found for this roll number.")
        return

    name = input("Enter New Student Name: ")
    if not validate_name(name):
        print("Invalid name! Name cannot contain numbers.")
        return

    marks = []
    for subject in ['Physics', 'Chemistry', 'Math']:
        mark = input(f"Enter new marks for {subject} (0-100): ")
        if not validate_mark(mark):
            print(f"Invalid mark for {subject}! Please enter a number between 0 and 100.")
            return
        marks.append(int(mark))

    student_dict[roll_number] = {'Name': name, 'Marks': marks}
    print("Student record updated successfully!")


def delete_student(student_dict):
    roll_number = input("Enter Roll Number to Delete: ")
    if not validate_roll_number(roll_number):
        print("Invalid roll number! Please enter a number between 1 and 100.")
        return

    if not check_record_exists(student_dict, roll_number):
        print("No record found for this roll number.")
        return

    del student_dict[roll_number]
    print("Student record deleted successfully!")


def stud_crud():
    student_dict = {}

    while True:
        print("\nMenu:")
        print("1. Create Student Record")
        print("2. View Student Record")
        print("3. Update Student Record")
        print("4. Delete Student Record")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_student(student_dict)
        elif choice == '2':
            view_student(student_dict)
        elif choice == '3':
            update_student(student_dict)
        elif choice == '4':
            delete_student(student_dict)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


stud_crud()
