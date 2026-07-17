import json

def save_students(students):
    data = []
    for student in students:
        s = {"name" : student.name, "roll" : student.roll , "age" : student.age}
        data.append(s)
    with open("students.json","w") as f:
        json.dump(data,f)
    # json.dump(students)


def load_students(students):
    try:
        with open("students.json","r") as f:
            data = json.load(f)
        
        for item in data:
            student = Student(item["name"],item["roll"],item["age"])
            students.append(student)

    except FileNotFoundError:
        save_students(students)

    except json.JSONDecodeError:
        print("students.json is corrupted. Starting with an empty list.")
        save_students(students)


def add_student(students):
    print("|| Enter Student Detail ||")
    try:
        name = input("Enter Name :")
        roll = int(input("Enter Roll No. :"))
        age = int(input("Enter Age :"))

        for student in students:
            if student.roll == roll:
                print("Roll no. Already Exist")
                return None
            
        s = Student(name,roll,age)
        return s
    except ValueError:
        print("Invalid details")

    

def display_students(students):
    if len(students) == 0:
        print("No Student Found")
    else:
        for student in students:
            print("Name : ",student.name,"|| Roll : ",student.roll,"|| Age : ",student.age)

def delete_student(students):
    try:
        roll = int(input("Enter Roll no. "))
        for student in students:
            if student.roll == roll:
                students.remove(student)
                print("Student Deleted Successfully !!!")
                break
        else:
            print("Student Does not exist")

    except ValueError:
        print("Invalid Roll no.")
    
def search_student(students):
    try:
        roll = int(input("Enter Roll no. "))
        for student in students:
            if student.roll == roll:
                print("Name : ",student.name)
                print("Roll : ",student.roll)
                print("Age : ",student.age)
                break
        else:
            print("Student Does not exist")
    except ValueError:
        print("Invalid Roll no.")

def update_student(students):
    try:
        roll = int(input("Enter Roll no. "))
        for student in students:
            if student.roll == roll:
                name = input("Enter updated name :")
                age = int(input("Enter Updates age :"))
                student.name = name
                student.age = age
                print("Updated Successfully !!!")
                break
        else:
            print("Student is not present")
    except ValueError:
        print("Invalid Roll no.")



class Student:
    def __init__(self,name,roll,age):
        self.name = name
        self.roll = roll
        self.age = age
        

students = []

# s1 = student("atharva",42,18)
# print(s1.name)


load_students(students)




while True:

    print("\n1. ADD Student")
    print("2. Display ALL Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Count Student")
    print("7. Exit\n")

    try:
        choice = int(input("Enter Your Choice: "))

        if choice==1:
            new = add_student(students)
            if new is None:
                pass

            else:
                students.append(new)
                save_students(students)

        elif choice ==2:
            display_students(students)

        elif choice == 3:
            delete_student(students)
            save_students(students)

        elif choice == 4:
            search_student(students)

        elif choice == 5:
            update_student(students)
            save_students(students)

        elif choice == 6:
            print("Total Students  ",len(students))

        elif choice == 7:
            break;

        else :
            print("Invalid Input")

    except ValueError:
        print("Enter Valid Choice")

    
