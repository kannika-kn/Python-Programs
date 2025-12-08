class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.__marks = {}  # Encapsulated (private) mark storage

    def add_marks(self, subject, mark):
        self.__marks[subject] = mark

    def get_average(self):
        if not self.__marks:
            return 0
        return sum(self.__marks.values()) / len(self.__marks)

    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def is_pass(self):
        return all(mark >= 35 for mark in self.__marks.values())

    def generate_report(self):
        print("\n===== Report Card =====")
        print(f"Name       : {self.name}")
        print(f"Roll No.   : {self.roll_number}")
        print("\nMarks:")
        for subject, mark in self.__marks.items():
            print(f"  {subject}: {mark}")
        print(f"\nAverage    : {self.get_average():.2f}")
        print(f"Grade      : {self.get_grade()}")
        print(f"Result     : {'Pass' if self.is_pass() else 'Fail'}")
        print("========================\n")


# Main program
students = {}

while True:
    print("1. Add Student")
    print("2. Enter Marks")
    print("3. Generate Report")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        roll = int(input("Enter roll number: "))
        students[roll] = Student(name, roll)
        print("Student added successfully!\n")

    elif choice == '2':
        roll = int(input("Enter roll number: "))
        student = students.get(roll)
        if student:
            num_subjects = int(input("How many subjects? "))
            for _ in range(num_subjects):
                subject = input("Enter subject name: ")
                mark = int(input(f"Enter marks for {subject}: "))
                student.add_marks(subject, mark)
            print("Marks added successfully!\n")
        else:
            print("Student not found.\n")

    elif choice == '3':
        roll = int(input("Enter roll number: "))
        student = students.get(roll)
        if student:  
            student.generate_report()
        else:
            print("Student not found.\n")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.\n")
