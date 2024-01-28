# Goal: Get list of all students who passed an exam

# List of students with names and marks
students = [
    {"name": "Alice", "marks": [80, 92, 75, 88]},
    {"name": "Bob", "marks": [90, 85, 89, 78]},
    {"name": "Charlie", "marks": [76, 85, 92, 80]},
    {"name": "David", "marks": [88, 78, 85, 90]},
]

# Example 9 (corrected): Use lambda with map and any() to check if any student passed (scored above 40 in any subject)
any_student_passed = any(map(lambda student: any(mark > 40 for mark in student["marks"]), students))

print("\nExample 9 (corrected): Any Student Passed")
print(any_student_passed)
