import os

class Student:
    def __init__(self, rollno, name, marks1, marks2, marks3, marks4, marks5):
        self.rollno = rollno
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.marks4 = marks4
        self.marks5 = marks5
        self.totalmarks = marks1 + marks2 + marks3 + marks4 + marks5

def display():
    os.system("cls")
    print("\n---Student details----")
    print("{:<10} {:<30} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Rollno", "Name", "Maths-IV", "Computer Networks", "Graph Theory", "OOS", "Software Engineering", "Total Marks"))
    with open("student.txt", "rb") as fp:
        while True:
            data = fp.read()
            if not data:
                break
            st = Student(data)
            print("{:<10} {:<30} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(st.rollno, st.name, st.marks1, st.marks2, st.marks3, st.marks4, st.marks5, st.totalmarks))

if __name__ == "__main__":
    display()
