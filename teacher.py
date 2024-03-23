import os
from student import Student, display

def add_student():
    if not os.path.exists("student.txt"):
        with open("student.txt", "wb") as f:
            pass
    fp = open("student.txt", "ab")
    print("Enter name: ")
    name = input()
    print("Enter rollno: ")
    rollno = int(input())
    marks1 = int(input("Enter marks of Maths-IV: "))
    marks2 = int(input("Enter marks of Computer Networks: "))
    marks3 = int(input("Enter marks of Graph Theory: "))
    marks4 = int(input("Enter marks of OOS: "))
    marks5 = int(input("Enter marks of Software Engineering: "))
    total_marks = marks1 + marks2 + marks3 + marks4 + marks5
    student_data = f"{name} {rollno} {marks1} {marks2} {marks3} {marks4} {marks5} {total_marks}\n"
    fp.write(student_data.encode())
    fp.close()
    print("Student added successfully...")

def update_marks():
    roll_no = int(input("\n-----Update marks-----\nEnter rollno to update: "))
    with open("student.txt", "rb+") as fp:
        students = []
        while True:
            data = fp.read()
            if not data:
                break
            st = Student(data)
            if st.rollno == roll_no:
                print("Enter the new set of marks")
                marks1 = int(input("Enter marks of Maths-IV: "))
                marks2 = int(input("Enter marks of Computer Networks: "))
                marks3 = int(input("Enter marks of Graph Theory: "))
                marks4 = int(input("Enter marks of OOS: "))
                marks5 = int(input("Enter marks of Software Engineering: "))
                st = Student(roll_no, st.name, marks1, marks2, marks3, marks4, marks5)
                students.append(st)
                print("\nMarks updated successfully...")
            else:
                students.append(st)
        fp.seek(0)
        for st in students:
            fp.write(st)

def teacher():
    val = int(input("\n1. Add student\n2. Update marks\n3. Display marks\nEnter choice: "))
    if val == 1:
        add_student()
    elif val == 2:
        update_marks()
    elif val == 3:
        display()
    else:
        print("Invalid input")

if __name__ == "__main__":
    while True:
        print("\n1. Teacher\n2. Student\n0. Exit")
        val = int(input("Enter choice: "))
        if val == 1:
            teacher()
        elif val == 0:
            break
        else:
            print("Invalid input")
