__author__ = "Vivek"
__author_email__ = "vivekltp120@gmail.com"

students_data = [
    {
        "Name": "John",
        "Gender": "M",
        "DOB": "5/4/88",
        "Maths": 55,
        "Physics": 45,
        "Chemistry": 56,
        "English": 87,
        "Biology": 21,
        "Economics": 52,
        "History": 89,
        "Civics": 65
    },
    {
        "Name": "Suresh",
        "Gender": "M",
        "DOB": "4/5/87",
        "Maths": 75,
        "Physics": 55,
        "Chemistry": None,
        "English": 64,
        "Biology": 90,
        "Economics": 61,
        "History": 58,
        "Civics": 2
    },
    {
        "Name": "Ramesh",
        "Gender": "M",
        "DOB": "25/5/1989",
        "Maths": 25,
        "Physics": 54,
        "Chemistry": 89,
        "English": 76,
        "Biology": 95,
        "Economics": 87,
        "History": 56,
        "Civics": 74
    },
    {
        "Name": "Jessica",
        "Gender": "F",
        "DOB": "12/8/90",
        "Maths": 78,
        "Physics": 55,
        "Chemistry": 86,
        "English": 63,
        "Biology": 54,
        "Economics": 89,
        "History": 75,
        "Civics": 45
    },
    {
        "Name": "Jennifer",
        "Gender": "F",
        "DOB": "2/9/89",
        "Maths": 58,
        "Physics": 96,
        "Chemistry": 78,
        "English": 46,
        "Biology": 96,
        "Economics": 77,
        "History": 83,
        "Civics": 53
    }
]
import pandas as pd
df = pd.DataFrame(students_data)
print(df)
print(df.head)

subject=["Physics",
        "Chemistry",
        "English",
        "Biology",
        "Economics",
        "History",
        "Civics"]

for student in students_data:
    name= student.get("name")
    avg=0
    for key,value in student.items():
        if key in subject:
            if value is None:
                value=0
            avg+=value
    student["average"]=avg/(len(subject))

for student in students_data:
   print(student)

