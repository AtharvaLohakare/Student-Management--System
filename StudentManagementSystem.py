import json
import csv

def save_students(students):
    data = []
    for student in students:
        s = {"name" : student.name, "roll" : student.roll , "age" : student.age}
        data.append(s)
    with open("students.json","w") as f:
        json.dump(data,f)
    # json.dump(students)

def export_student_data(students):
    with open("students.csv","w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Roll", "Age"])
        for student in students:
            s = [student.name,student.roll,student.age]
            writer.writerow(s)


def import_student_data(students):
    try:
        with open("students.csv", "r", newline="") as f:
            reader = csv.reader(f)
            next(reader)
            for item in reader:
                name = item[0]
                roll = int(item[1])
                age = int(item[2])

                # Check duplicate roll number
                duplicate = False
                for student in students:
                    if student.roll == roll:
                        duplicate = True
                        break
                if not duplicate:
                    students.append(Student(name, roll, age))

    except FileNotFoundError:
        print("student.csv not found!")

    except ValueError:
        print("Invalid data in CSV file!")

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
        print("=" * 40)
        print(f"{"No.":<5}{'Name':<15}{'Roll no.':<15}{'age'}")
        print("=" * 40)
        # for student in students:
        for i ,  student in enumerate(students,start=1):
            print(f"{i:<5}{student.name:<15}{student.roll:<15}{student.age}")
        print("=" * 40)

def find_student(students):
    try:
        roll_name = input("Enter Roll no. or name ")
        if roll_name.isdigit():
            roll_name = int(roll_name)
        else:
            roll_name = roll_name.lower()
        
        for student in students:
            if student.roll == roll_name or student.name.lower() == roll_name:
                return student
        else:
            return None

    except ValueError:
       print("Inavlid Detail !")

def delete_student(students):
    student = find_student(students)
    if student is not None:
        students.remove(student)
        print("Student DeletedSuccessfully !!!")
    else:
        print("Student Does not exist !")
    
def search_student(students):
    student = find_student(students)
    if student is not None:
        print("="*14,"StudentFound","="*14,"\n")
        print("Name : ",student.name)
        print("Roll : ",student.roll)
        print("Age : ",student.age)
        print("\n")
        print("="*40)
        
    else:
        print("Student Does not exist !")

def update_student(students):
    student = find_student(students)
    if student is not None:
        name = input("Enter new Name (leave blank to keep old name):")
        age = input("Enter new Age (leave blank to keep old age):")
        if name != "":
            student.name = name
        if age != "":
            student.age = int(age)
        print("Updated Successfully !!!")
    else:
        print("Student Does not exist !")

def statistics(students):
    print("="*14,"Statistics","="*14,"\n")
    

    print(f"Total Students : {len(students)}")

    if len(students) == 0:
        print("Data unavailable")
    else:
        total = 0
        for student in students:
            total += student.age
        print(f"Average Age : {total / len(students):.2f}")

        students.sort(key=lambda student: student.age)

        youngest = students[0]

        print(f"Youngest Student : {youngest.name} {youngest.age} {youngest.roll}")
        students.sort(key=lambda student: student.age, reverse=True)

        oldest = students[0]
        print(f"Oldest Student : {oldest.name} {oldest.age} {oldest.roll}")

        print("="*40)

class Student:
    def __init__(self,name,roll,age):
        self.name = name
        self.roll = roll
        self.age = age
        

students = []

# s1 = student("atharva",42,18)
# print(s1.name)


# load_students(students) for json
import_student_data(students)



while True:

    print("\n1. ADD Student")
    print("2. Display ALL Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Count Student")
    print("7. Sort Student")
    print("8. Statistics")
    print("9. Exit\n")

    try:
        choice = int(input("Enter Your Choice: "))

        if choice==1:
            new = add_student(students)
            if new:
                students.append(new)
                save_students(students)
                export_student_data(students)

        elif choice ==2:
            display_students(students)

        elif choice == 3:
            delete_student(students)
            save_students(students)
            export_student_data(students)

        elif choice == 4:
            search_student(students)

        elif choice == 5:
            update_student(students)
            save_students(students)
            export_student_data(students)

        elif choice == 6:
            print("Total Students  ",len(students))
        
        elif choice == 7:
            print("1. Name (A-Z)")
            print("2. Name (Z-A)")
            print("3. Age (Low-High)")
            print("4. Age (High-Low)")
            print("5. Roll (Low-High)")
            print("6. Roll (High-Low)")
            sort_choice = int(input("Enter Choice :"))

            if sort_choice == 1:
                students.sort(key = lambda student: student.name)
                save_students(students)
                export_student_data(students)
                print("Sorted Successfully !")

            if sort_choice == 2:
                students.sort(key = lambda student: student.name, reverse = True)
                save_students(students)
                export_student_data(students)
                print("Sorted Successfully !")

            elif sort_choice == 3:
                students.sort(key = lambda student: student.age)
                save_students(students)
                export_student_data(students)
                print("Sorted Successfully !")

            elif sort_choice == 4:
                students.sort(key = lambda student: student.age, reverse = True)
                save_students(students)
                export_student_data(students)
                print("Sorted Successfully !")

            elif sort_choice == 5:
                students.sort(key = lambda student: student.roll)
                save_students(students)
                export_student_data(students)
                print("Sorted Successfully !")

            elif sort_choice == 6:
                students.sort(key = lambda student: student.roll, reverse = True)
                save_students(students)
                export_student_data(students)
                print("Sorted Successfully !")
            
            else:
                print("Invalid Input")
        
       elif choice==8:
            statistics(students) 
                        
        elif choice == 9:
            break;

        else :
            print("Invalid Input")

    except ValueError:
        print("Enter Valid Choice")
