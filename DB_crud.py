import mysql.connector


# def add_teacher(cursor, name, qualification):
#     cursor.execute("INSERT INTO teacher (name, qualification) VALUES (%s, %s)", (name, qualification))
#     connection.commit()
#     if cursor.rowcount == 1:
#         return True
#     else:
#         return False


def view_teachers(cursor):
    sql = "Select * from teacher"
    cursor.execute(sql)
    return cursor.fetchall()


def view_subjects(cursor):
    sql = "Select * from subject"
    cursor.execute(sql)
    return cursor.fetchall()


def assign_teacher(connection, cursor, t_id, s_id):
    sql = "INSERT INTO teach_sub (t_id, s_id, status) VALUES (%s, %s, 'active')"
    cursor.execute(sql, (t_id, s_id))
    if cursor.rowcount == 1:
        connection.commit()
        return True
    else:
        return False


def view_assignments(cursor):
    sql = "Select teach_sub.id,teacher.name,subject.name from teacher,subject,teach_sub where teacher.id=teach_sub.t_id and subject.id=teach_sub.s_id and status= 'active' ORDER BY teach_sub.id"
    cursor.execute(sql)
    return cursor.fetchall()


def update_assignment(connection, cursor, id, t_id, s_id, status):
    sql = "UPDATE teach_sub SET t_id = %s , s_id = %s , status = %s where id = %s"
    cursor.execute(sql, (t_id, s_id, status, id))
    connection.commit()
    if cursor.rowcount <= 1:
        return True
    else:
        return False


def delete_assignment(cursor, id):
    sql = "DELETE from teach_sub where id = %s"
    cursor.execute(sql, (id,))
    connection.commit()
    if cursor.rowcount <= 1:
        return True
    else:
        return False


def teachers_sub(cursor, id):
    sql = "Select subject.name from subject,teach_sub where subject.id = teach_sub.s_id and t_id = %s"
    cursor.execute(sql, (id,))
    return cursor.fetchall()


def count_prac(cursor):
    sql = "Select count(teach_sub.id) from teach_sub,subject where teach_sub.s_id=subject.id and subject.type in ('p','t/p')"
    cursor.execute(sql)
    return cursor.fetchall()


connection = (mysql.connector.connect
              (user='root', password='',
               host='localhost',
               database='teacher')
              )
if connection.is_connected():
    cursor = connection.cursor()
    while True:
        print(
            "Menu:\n1. View Teachers\n2. View Subjects\n3. Assign Subject to Teacher\n4. View Active "
            "assignments\n5.Update assignment\n6.Delete assignment\n7.Fetch all assignments of a specific "
            "teacher\n8.Fetch count of teachers who have practical subjects\nType 'stop' to exit")
        choice = input("Enter your choice: ")
        if choice == 'stop':
            break
        # if choice == '1':
        #     name = input("Enter name: ")
        #     qualification = input("Enter qualification")
        #     if add_teacher(cursor, name, qualification):
        #         print("Record added successfully")
        #     else:
        #         print("Record could not be added")
        elif choice == '1':
            teachers = view_teachers(cursor)
            for teacher in teachers:
                print("Teacher id\tName\t Qualification")
                print(f"{teacher[0]}\t\t\t{teacher[1]}\t\t\t{teacher[2]}\n")
        elif choice == '2':
            subjects = view_subjects(cursor)
            for subject in subjects:
                print("Subject id\tSubject\tType")
                print(f"{subject[0]}\t\t\t{subject[1]}\t\t{subject[2]}\n")
        elif choice == '3':
            t_id = int(input("Enter teacher id: "))
            s_id = int(input("Enter subject id: "))
            if assign_teacher(connection, cursor, t_id, s_id):
                print("Teacher assigned to subject")
            else:
                print("Teacher could not be assigned")
        elif choice == '4':
            assignments = view_assignments(cursor)
            print("\n\nACTIVE ASSIGNMENTS: ")
            for assignment in assignments:
                print(f"{assignment[0]} . {assignment[1]}:{assignment[2]}")
        elif choice == '5':
            id = int(input("Enter assignment number to be updated: "))
            t_id = int(input("Enter teacher id: "))
            s_id = int(input("Enter subject id: "))
            status = input("Enter status(active/inactive)")
            update_assignment(connection, cursor, id, t_id, s_id, status)
        elif choice == '6':
            id = int(input("Enter assignment number to be deleted: "))
            if delete_assignment(cursor, id):
                print("Record deleted")
            else:
                print("Some error occurred")
        elif choice == '7':
            id = int(input("Enter teacher id: "))
            subjects = teachers_sub(cursor, id)
            print("Subjects taught by the teacher: ")
            for subject in subjects:
                print(subject[0])
        elif choice == '8':
            cnt = count_prac(cursor)
            print(f"COUNT : {cnt[0][0]}")
        else:
            print("Invalid choice, please try again.")

    # sql = "select * from teacher"
    # cursor.execute(sql)
    # result = cursor.fetchall()
    # for i in result:
    #     print(i)
    connection.close()
else:
    print("Connection failed")
