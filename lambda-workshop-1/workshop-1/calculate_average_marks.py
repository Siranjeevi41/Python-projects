# List of students with names and marks
students = [
    {"name": "Alice", "marks": [80, 92, 80, 88]},
    {"name": "Bob", "marks": [90, 85, 89, 78]},
    {"name": "Charlie", "marks": [76, 85, 92, 80]},
    {"name": "David", "marks": [88, 78, 85, 90]},
]

# Example 1: Calculate the average marks for each student using lambda and map
average_marks = list(map(lambda student: (student["name"], sum(student["marks"]) / len(student["marks"])), students))

print("Example 1: Average Marks")
print(average_marks)

# Example 2: Filter students who have scored more than a certain threshold using lambda and filter
passing_students = list(filter(lambda student: all(mark >= 80 for mark in student["marks"]), students))

print("\nExample 2: Passing Students")
print(passing_students)
