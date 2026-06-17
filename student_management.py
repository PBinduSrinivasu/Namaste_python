import json

FILE_NAME = "students.json"


# Load students from file
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


# Save students to file
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Add student
def add_student():
    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["Roll No"] == roll_no:
            print("Roll Number already exists!")
            return

    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    student = {
        "Roll No": roll_no,
        "Name": name,
        "Marks": marks
    }

    students.append(student)
    save_students()

    print("Student Added Successfully!")


# View students
def view_students():
    if not students:
        print("No Students Found")
        return

    print("\nStudent Records")
    print("-" * 40)

    for student in students:
        print(
            f"Roll No: {student['Roll No']}, "
            f"Name: {student['Name']}, "
            f"Marks: {student['Marks']}"
        )


# Search student
def search_student():
    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["Roll No"] == roll_no:
            print("\nStudent Found")
            print(student)
            return

    print("Student Not Found")


# Update marks
def update_marks():
    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["Roll No"] == roll_no:
            new_marks = float(input("Enter New Marks: "))
            student["Marks"] = new_marks

            save_students()
            print("Marks Updated Successfully!")
            return

    print("Student Not Found")


# Delete student
def delete_student():
    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["Roll No"] == roll_no:
            students.remove(student)

            save_students()
            print("Student Deleted Successfully!")
            return

    print("Student Not Found")


# Average marks
def calculate_average():
    if not students:
        print("No Students Found")
        return

    total = 0

    for student in students:
        total += student["Marks"]

    average = total / len(students)

    print(f"Average Marks: {average:.2f}")


# Find topper
def find_topper():
    if not students:
        print("No Students Found")
        return

    topper = students[0]

    for student in students:
        if student["Marks"] > topper["Marks"]:
            topper = student

    print("\nTopper Details")
    print(
        f"Roll No: {topper['Roll No']}, "
        f"Name: {topper['Name']}, "
        f"Marks: {topper['Marks']}"
    )


# Main Program
students = load_students()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Calculate Average")
    print("7. Find Topper")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        calculate_average()

    elif choice == "7":
        find_topper()

    elif choice == "8":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")