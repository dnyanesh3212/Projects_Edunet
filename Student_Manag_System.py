import csv
from colorama import Fore, Style, init

init(autoreset=True)

class StudentManagementSystem:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.load_students()

    def load_students(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.students = [row for row in reader]
        except FileNotFoundError:
            self.students = []

    def save_students(self):
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ["ID", "Name", "Age", "Course"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.students)

    def add_student(self):
        student_id = input(Fore.CYAN + "Enter Student ID: ")
        name = input(Fore.CYAN + "Enter Student Name: ")
        age = input(Fore.CYAN + "Enter Student Age: ")
        course = input(Fore.CYAN + "Enter Course: ")
        
        self.students.append({"ID": student_id, "Name": name, "Age": age, "Course": course})
        self.save_students()
        print(Fore.GREEN + "Student record added successfully!\n")

    def view_students(self):
        if not self.students:
            print(Fore.RED + "No student records found.\n")
        else:
            print(Fore.YELLOW + "\nStudent Records:")
            for student in self.students:
                print(Fore.BLUE + f"ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Course: {student['Course']}")
            print()

    def search_student(self):
        search_id = input(Fore.CYAN + "Enter Student ID to search: ")
        found = False
        for student in self.students:
            if student["ID"] == search_id:
                print(Fore.GREEN + f"Found: ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Course: {student['Course']}\n")
                found = True
                break
        if not found:
            print(Fore.RED + "Student not found.\n")

    def update_student(self):
        search_id = input(Fore.CYAN + "Enter Student ID to update: ")
        for student in self.students:
            if student["ID"] == search_id:
                student["Name"] = input(Fore.YELLOW + f"Enter new name ({student['Name']}): ") or student["Name"]
                student["Age"] = input(Fore.YELLOW + f"Enter new age ({student['Age']}): ") or student["Age"]
                student["Course"] = input(Fore.YELLOW + f"Enter new course ({student['Course']}): ") or student["Course"]
                self.save_students()
                print(Fore.GREEN + "Student record updated successfully!\n")
                return
        print(Fore.RED + "Student not found.\n")

    def delete_student(self):
        search_id = input(Fore.CYAN + "Enter Student ID to delete: ")
        for student in self.students:
            if student["ID"] == search_id:
                self.students.remove(student)
                self.save_students()
                print(Fore.GREEN + "Student record deleted successfully!\n")
                return
        print(Fore.RED + "Student not found.\n")

    def menu(self):
        while True:
            print(Fore.MAGENTA + "\nStudent Management System")
            print(Fore.CYAN + "1. Add Student")
            print(Fore.CYAN + "2. View All Students")
            print(Fore.CYAN + "3. Search Student")
            print(Fore.CYAN + "4. Update Student Information")
            print(Fore.CYAN + "5. Delete Student Record")
            print(Fore.CYAN + "6. Exit")
            
            choice = input(Fore.YELLOW + "Enter your choice: ")
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                print(Fore.RED + "Exiting program. Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice! Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    system = StudentManagementSystem()
    system.menu()
