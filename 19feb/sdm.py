# ----------------------------------------
# Student Data Manager
# ----------------------------------------

def assign_grade(marks):
    """
    Assigns grade based on marks.
    """
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def main():
    students = {}

    print("=== Student Data Manager ===\n")

    # Input data for 5 students
    for i in range(1, 6):
        name = input(f"Enter name of student {i}: ").strip()
        
        while True:
            try:
                marks = float(input(f"Enter marks for {name}: "))
                if 0 <= marks <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter numeric marks.")

        students[name] = {
            "marks": marks,
            "grade": assign_grade(marks)
        }

    # Calculate topper
    topper = max(students, key=lambda x: students[x]["marks"])
    highest_marks = students[topper]["marks"]

    # Calculate class average
    total_marks = sum(student["marks"] for student in students.values())
    average = total_marks / len(students)

    # Display Results
    print("\n=== Student Report ===")
    for name, data in students.items():
        print(f"{name} -> Marks: {data['marks']} | Grade: {data['grade']}")

    print("\n=== Summary ===")
    print(f"Topper: {topper} with {highest_marks} marks 🏆")
    print(f"Class Average: {average:.2f}")


if __name__ == "__main__":
    main()