def add_student():
    print("|| Enter Student Detail ||")
    name = input("Enter Name :")
    roll = int(input("Enter Roll No. :"))
    age = int(input("Enter Age :"))
    s = Student(name,roll,age)
    return s

def display_students(students):
    if len(students) == 0:
        print("No Student Found")
    else:
        for Student in students:
            print("Name : ",Student.name,"|| Roll : ",Student.roll,"|| Age : ",Student.age)

def delete_student(students):
    roll = int(input("Enter Roll no. "))
    for Student in students:
        if Student.roll == roll:
            students.remove(Student)
            print("Student Deleted Successfully !!!")
            break
    else:
        print("Student Does not exist")
    
def search_student(students):
    roll = int(input("Enter Roll no. "))
    for Student in students:
        if Student.roll == roll:
            print("Name : ",Student.name)
            print("Roll : ",Student.roll)
            print("Age : ",Student.age)
            break
    else:
        print("Student Does not exist")

def update_student(students):
    roll = int(input("Enter Roll no. "))
    for Student in students:
        if Student.roll == roll:
            name = input("Enter updated name :")
            age = int(input("Enter Updates age :"))
            Student.name = name
            Student.age = age
            print("Updated Successfully !!!")
            break
    else:
        print("Student is not present")
    


class Student:
    def __init__(self,name,roll,age):
        self.name = name
        self.roll = roll
        self.age = age
        

students = []

# s1 = student("atharva",42,18)
# print(s1.name)

while True:

    print("1. ADD Student")
    print("2. Display ALL Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Count Student")
    print("7. Exist")
    choice = int(input("Enter Your Choice: "))

    if choice==1:
        students.append(add_student())

    elif choice ==2:
        display_students(students)

    elif choice == 3:
        delete_student(students)

    elif choice == 4:
        search_student(students)

    elif choice == 5:
        update_student(students)

    elif choice == 6:
        print("Total Students  ",len(students))

    elif choice == 7:
        break;

    else :
        print("Invalid Input")

    