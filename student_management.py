import json

students = []  # List to store student records

try:
    with open("students.json", "r") as file:
        students = json.load(file)
except:
    students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")
    student = {
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("\n Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found.")
        return
    print("\n-------- Student List --------")

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print("-----------------------------")
    
def search_student():
    search_name = input("Enter student name to search: ")

    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent found:")
            print(student)
            found = True
            break
 

    if not found:
        print("\nStudent not found.")

def update_student():
    search_name = input("Enter student name to update: ")
    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\n Current student details:")
            print(student)

            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")   
            student["course"] = input("Enter new course: ")
            print("\n Student details updated successfully!")
            found = True
            break

    if not found:
        print("\nStudent not found.")

def delete_student():
    search_name = input("Enter student name to delete: ")
    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            students.remove(student)
            print("\n Student deleted successfully!")
            found = True
            break

    if not found:
        print("\nStudent not found.")

while True:
    print("\n-------- Student Management System --------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("\n Thank you for using the Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")

    

