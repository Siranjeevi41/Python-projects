# List of students with names and marks
students = [
    {"name": "Alice", "marks": [80, 92, 75, 88]},
    {"name": "Bob", "marks": [90, 85, 89, 78]},
    {"name": "Charlie", "marks": [76, 85, 92, 80]},
    {"name": "David", "marks": [88, 78, 85, 90]},
]

# Example 11: Use lambda with sorted to sort students by their lowest mark
sorted_by_lowest_mark = sorted(students, key=lambda student: min(student["marks"]))

print("\nExample 11: Sorted Students by Lowest Mark")
for student in sorted_by_lowest_mark:
    print(f"{student['name']}: {min(student['marks'])}")

# Example 12: Use lambda with filter to get students who scored below a certain threshold in any subject
below_threshold_students = list(filter(lambda student: any(mark < 60 for mark in student["marks"]), students))

print("\nExample 12: Students Below Threshold in Any Subject")
print(below_threshold_students)
