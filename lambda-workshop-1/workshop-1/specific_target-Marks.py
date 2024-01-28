# List of students with names and marks
students = [
    {"name": "Alice", "marks": [80, 92, 75, 88]},
    {"name": "Bob", "marks": [90, 85, 89, 78]},
    {"name": "Charlie", "marks": [76, 85, 92, 80]},
    {"name": "David", "marks": [88, 78, 85, 90]},
]

# Example 6: Extract names of students with a specific mark using lambda and filter
target_mark = 85
students_with_target_mark = list(filter(lambda student: target_mark in student["marks"], students))

print("\nExample 6: Students with Target Mark")
print(students_with_target_mark)

# Example 7: Calculate the total marks for each student using lambda and map
total_marks = list(map(lambda student: (student["name"], sum(student["marks"])), students))

print("\nExample 7: Total Marks")
print(total_marks)

# Example 8: Use lambda with reduce to find the overall class average
from functools import reduce

class_average = reduce(lambda acc, student: acc + sum(student["marks"]), students, 0) / len(students)

print("\nExample 8: Class Average")
print(class_average)
