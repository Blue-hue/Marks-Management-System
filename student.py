import pandas as pd
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
    df = pd.read_csv("student.csv")
    sorted_df = df.sort_values(by='Total Marks', ascending=False)
    print(sorted_df)

if __name__=="__main__":
    display()