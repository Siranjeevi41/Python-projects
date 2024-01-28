# List of students with names and marks
students = [
    {"name": "Alice", "marks": [80, 92, 75, 88]},
    {"name": "Bob", "marks": [70, 85, 89, 78]},
    {"name": "Charlie", "marks": [76, 85, 92, 80]},
    {"name": "David", "marks": [88, 78, 85, 90]},
]

# Example 13: Use lambda with map to calculate the weighted average of marks for each student
weights = [0.25, 0.25, 0.2, 0.3]
weighted_average = list(map(lambda student: (student["name"], sum(mark * weight for mark, weight in zip(student["marks"], weights))), students))

print("\nExample 13: Weighted Average Marks")
print(weighted_average)

# Example 14: Use lambda with reduce to find the student with the highest total marks
from functools import reduce

highest_total_marks_student = reduce(lambda acc, student: acc if sum(acc["marks"]) > sum(student["marks"]) else student, students)

print("\nExample 14: Student with Highest Total Marks")
print(highest_total_marks_student["name"])

# Example 15: Use lambda with sorted to sort students by the total sum of their marks
sorted_by_total_marks = sorted(students, key=lambda student: sum(student["marks"]), reverse=True)

print("\nExample 15: Sorted Students by Total Marks")
for student in sorted_by_total_marks:
    print(f"{student['name']}: {sum(student['marks'])}")
