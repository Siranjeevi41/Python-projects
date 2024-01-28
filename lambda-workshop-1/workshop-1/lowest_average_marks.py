# List of students with names and marks
students = [
    {"name": "Alice", "marks": [100, 102, 75, 88]},
    {"name": "Bob", "marks": [90, 85, 89, 78]},
    {"name": "Charlie", "marks": [76, 85, 92, 80]},
    {"name": "David", "marks": [88, 78, 85, 90]},
]

# Example 3: Find the student with the highest average marks using lambda and min
highest_scorer = min(students, key=lambda student: sum(student["marks"]) / len(student["marks"]))

print("\nExample 3: Highest Scorer")
print(highest_scorer["name"])

# Example 4: Sort students based on their average marks using lambda and sorted
sorted_students = sorted(students, key=lambda student: sum(student["marks"]) / len(student["marks"]), reverse=True)

print("\nExample 4: Sorted Students by Average Marks")
for student in sorted_students:
    print(f"{student['name']}: {sum(student['marks']) / len(student['marks']):.2f}")

# Example 5: Using lambda with conditional expression to categorize students
category = lambda student: "Excellent" if all(mark >= 90 for mark in student["marks"]) else "Good"

student_categories = {student["name"]: category(student) for student in students}

print("\nExample 5: Student Categories")
print(student_categories)
