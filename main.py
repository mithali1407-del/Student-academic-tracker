def add_record():

    student_name = input("Enter Student Name : ")
    student_roll = input("Enter Roll Number : ")

    subject1 = int(input("Enter Subject 1 Marks : "))
    subject2 = int(input("Enter Subject 2 Marks : "))
    subject3 = int(input("Enter Subject 3 Marks : "))
    subject4 = int(input("Enter Subject 4 Marks : "))
    subject5 = int(input("Enter Subject 5 Marks : "))

    total_marks = subject1 + subject2 + subject3 + subject4 + subject5 
    average_marks = total_marks / 5

    if average_marks >= 90:
        grade = "A"

    elif average_marks >= 60:
        grade = "B"

    else:
        grade = "C"

    with open("students.txt", "a") as file:

        file.write(
            f"{student_name},{student_roll},{total_marks},{average_marks},{grade}\n"
        )

    print("\nRecord Added Successfully")


def show_records():

    try:

        with open("students.txt", "r") as file:

            records = file.readlines()

            if not records:

                print("\nNo Records Available")

            else:

                print("\n===== STUDENT RECORDS =====")

                for data in records:

                    student = data.strip().split(",")

                    print(f"""
Name       : {student[0]}
Roll No    : {student[1]}
Total      : {student[2]}
Average    : {student[3]}
Grade      : {student[4]}
-------------------------------
""")

    except FileNotFoundError:

        print("\nFile Not Found")


def remove_record():

    roll_number = input("Enter Roll Number to Remove : ")

    found = False

    with open("students.txt", "r") as file:

        all_records = file.readlines()

    with open("students.txt", "w") as file:

        for data in all_records:

            student = data.strip().split(",")

            if student[1] != roll_number:

                file.write(data)

            else:

                found = True

    if found:

        print("\nRecord Removed Successfully")

    else:

        print("\nRecord Not Found")


while True:

    print("""
======= STUDENT RECORD SYSTEM =======

1. Add Record
2. View Records
3. Delete Record
4. Exit

=====================================
""")

    user_choice = input("Enter Your Choice : ")

    if user_choice == '1':

        add_record()

    elif user_choice == '2':

        show_records()

    elif user_choice == '3':

        remove_record()

    elif user_choice == '4':

        print("\nProgram Closed")
        break

    else:

        print("\nInvalid Choice")
