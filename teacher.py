import os
import pandas as pd
from student import *

def add_student():
    if not os.path.exists("student.csv"):
        df = pd.DataFrame(columns=["Rollno", "Name", "Maths-IV", "Computer Networks", "Graph Theory", "OOS", "Software Engineering"])
        df.to_csv("student.csv", index=False)

    rollno = int(input("Enter rollno: "))
    name = input("Enter name: ")
    marks1 = int(input("Enter marks of Maths-IV: "))
    marks2 = int(input("Enter marks of Computer Networks: "))
    marks3 = int(input("Enter marks of Graph Theory: "))
    marks4 = int(input("Enter marks of OOS: "))
    marks5 = int(input("Enter marks of Software Engineering: "))
    
    total_marks = marks1 + marks2 + marks3 + marks4 + marks5
    student_data = {"Rollno": rollno, "Name": name, "Maths-IV": marks1, "Computer Networks": marks2, 
                    "Graph Theory": marks3, "OOS": marks4, "Software Engineering": marks5, "Total Marks": total_marks}
    
    df = pd.read_csv("student.csv")
    df = df._append(student_data, ignore_index=True)
    df.to_csv("student.csv", index=False)

    print("Student added successfully...")

def update_marks():
    roll_no = int(input("\n-----Update marks-----\nEnter rollno to update: "))
    df = pd.read_csv("student.csv")

    for index, row in df.iterrows():
        if row["Rollno"] == roll_no:
            print("Enter the new set of marks")
            marks1 = int(input("Enter marks of Maths-IV: "))
            marks2 = int(input("Enter marks of Computer Networks: "))
            marks3 = int(input("Enter marks of Graph Theory: "))
            marks4 = int(input("Enter marks of OOS: "))
            marks5 = int(input("Enter marks of Software Engineering: "))

            total_marks = marks1 + marks2 + marks3 + marks4 + marks5
            df.at[index, "Maths-IV"] = marks1
            df.at[index, "Computer Networks"] = marks2
            df.at[index, "Graph Theory"] = marks3
            df.at[index, "OOS"] = marks4
            df.at[index, "Software Engineering"] = marks5
            df.at[index, "Total Marks"] = total_marks

            df.to_csv("student.csv", index=False)
            print("\nMarks updated successfully...")
            return

    print("\nStudent not found...")

def teacher():
    while True:
        print("\n1. Add student\n2. Update marks\n3. Display marks\n0. Exit")
        val = int(input("Enter choice: "))
        if val == 1:
            add_student()
        elif val == 2:
            update_marks()
        elif val == 3:
            display()
        elif val == 0:
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    teacher()
