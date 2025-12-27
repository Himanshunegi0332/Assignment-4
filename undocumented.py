import json
import os
from typing import Dict, List, Optional


def display_menu() -> None:
    print("-" * 30)
    print(
"""1. Add student
2. Add grade
3. Show average for student 
4. Show all students
5. Save to file 
6. Load from file 
7. Exit"""
    )
    print("-" * 30)


students: Dict[str, List[float]] = {
    "Max": [85, 92, 78],
    "Marina": [90, 88],
    "Ashley": [65, 74, 50],
    "Bonnie": [99, 87]
}


def add_student(students: Dict[str, List[float]], name: str) -> None:
    if name not in students:
        students[name] = []
    else:
        print(f"student {name} already exists")


def add_grade(students: Dict[str, List[float]], name: str, grade: float) -> None:
    if name in students:
        if 0 <= grade <= 100:
            students[name].append(grade)
        else:
            print("grade must be between 0 and 100")
    else:
        print(f"student {name} does not exist")


def average(students: Dict[str, List[float]], name: str) -> Optional[float]:
    if name in students and students[name]:
        return sum(students[name]) / len(students[name])
    else:
        print(f"{name} has no grades")
        return None


def save_to_file(students: Dict[str, List[float]], filename: str) -> None:
    with open(filename, "w") as file:
        json.dump(students, file)


def load_from_file(filename: str) -> Dict[str, List[float]]:
    if not os.path.exists(filename):
        print("file does not exist")
        return {}

    with open(filename, "r") as file:
        return json.load(file)


def delete_student(students: Dict[str, List[float]], name: str) -> None:
    if name in students:
        del students[name]
        print(f"deleted student {name}")
    else:
        print(f"student {name} does not exist")


def delete_grade(students: Dict[str, List[float]], name: str, grade: float) -> None:
    if name not in students:
        print(f"student {name} does not exist")
        return
    if grade not in students[name]:
        print(f"{name} does not have grade {grade}")
        return
    students[name].remove(grade)
    print(f"removed grade {grade} from {name}")


while True:
    filename: str = "students.json"

    display_menu()
    choice: str = input("choose an option: ")

    if choice == "1":
        name: str = input("enter student name: ")
        add_student(students, name)

    elif choice == "2":
        name: str = input("enter student name: ")
        grade: float = float(input("enter grade (0–100): "))
        add_grade(students, name, grade)

    elif choice == "3":
        name: str = input("enter student name: ")
        result: Optional[float] = average(students, name)
        if result is not None:
            print(f"average grade for {name}: {round(result, 2)}")

    elif choice == "4":
        for name, grades in students.items():
            print(f"{name}: {grades}")

    elif choice == "5":
        save_to_file(students, filename)
        print("saved")

    elif choice == "6":
        students = load_from_file(filename)
        print("loaded")

    elif choice == "7":
        break

    else:
        print("invalid option")
