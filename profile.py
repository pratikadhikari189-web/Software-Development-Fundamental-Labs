name=input("Enter your name:")
age=int(input("Enter your age:"))
course=(input ("Enter your course:"))
GPA=float(input("Enter your GPA:"))
Local_student_status=(input("Enter your Local_student_status:"))
Currentyear=2026
Birthyear=Currentyear-age
print("STUDENT PROFILE")
print(f"Your name is {name}")
print(f"Your age is {age}")
print(f"Your course is {course}")
print(f"Your GPA is {GPA}")
print(f"Yes" if Local_student_status else "No")

