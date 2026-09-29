def input_number_of_students() -> int:
    """Inputs and returns the total number of students in a class."""
    return int(input("Enter total number of students: "))


def input_student_info(student_count: int) -> list:
    """Inputs information (id, name, DoB) for all students."""
    students = []
    for i in range(student_count):
        print(f"\n--- Student {i + 1} Info ---")
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Date of Birth (DoB): ")
        students.append({
            "id": student_id,
            "name": name,
            "dob": dob
        })
    return students


def input_number_of_courses() -> int:
    """Inputs and returns the total number of courses."""
    return int(input("Enter total number of courses: "))


def input_course_info(course_count: int) -> list:
    """Inputs information (id, name) for all courses."""
    courses = []
    for i in range(course_count):
        print(f"\n--- Course {i + 1} Info ---")
        course_id = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        courses.append({
            "id": course_id,
            "name": name
        })
    return courses


def input_marks(students: list, courses: list, marks: dict) -> None:
    """Selects a course and inputs marks for all students in that course."""
    if not courses:
        print("No courses available. Please input course information first.")
        return
    if not students:
        print("No students available. Please input student information first.")
        return

    list_courses(courses)
    selected_course_id = input("\nEnter Course ID to input marks for: ")

    course_exists = any(c['id'] == selected_course_id for c in courses)
    if not course_exists:
        print("Course ID not found!")
        return

    if selected_course_id not in marks:
        marks[selected_course_id] = {}

    print(f"\n--- Inputting marks for course ID: {selected_course_id} ---")
    for student in students:
        mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
        marks[selected_course_id][student['id']] = mark


def list_courses(courses: list) -> None:
    """Lists all available courses."""
    print("\n================ LIST OF COURSES ================")
    if not courses:
        print("No courses found.")
        return
    for course in courses:
        print(f"ID: {course['id']:<10} | Name: {course['name']}")


def list_students(students: list) -> None:
    """Lists all available students."""
    print("\n================ LIST OF STUDENTS ================")
    if not students:
        print("No students found.")
        return
    for student in students:
        print(f"ID: {student['id']:<10} | Name: {student['name']:<20} | DoB: {student['dob']}")


def show_student_marks(courses: list, students: list, marks: dict) -> None:
    """Shows student marks for a given course."""
    if not courses or not students:
        print("Please ensure both students and courses are added first.")
        return

    course_id = input("\nEnter Course ID to view marks: ")
    course = next((c for c in courses if c['id'] == course_id), None)

    if not course:
        print("Course ID not found!")
        return

    if course_id not in marks or not marks[course_id]:
        print("No marks found for this course.")
        return

    print(f"\n================ MARKS FOR COURSE: {course['name']} ({course_id}) ================")
    for student in students:
        s_id = student['id']
        mark = marks[course_id].get(s_id, "N/A")
        print(f"ID: {s_id:<10} | Name: {student['name']:<20} | Mark: {mark}")


def main():
    students = []
    courses = []
    marks = {}  # Format: {course_id: {student_id: mark}}

    while True:
        print("\n" + "=" * 45)
        print("    STUDENT MARK MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a course")
        print("0. Exit")
        
        choice = input("Select an option (0-6): ")

        if choice == '1':
            num_students = input_number_of_students()
            students = input_student_info(num_students)
        elif choice == '2':
            num_courses = input_number_of_courses()
            courses = input_course_info(num_courses)
        elif choice == '3':
            input_marks(students, courses, marks)
        elif choice == '4':
            list_courses(courses)
        elif choice == '5':
            list_students(students)
        elif choice == '6':
            show_student_marks(courses, students, marks)
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please select between 0 and 6.")


if __name__ == "__main__":
    main()
       