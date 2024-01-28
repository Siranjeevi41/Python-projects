# List of students with names and marks
students = [
    {"name": "Alice", "marks": [80, 92, 75, 88]},
    {"name": "Bob", "marks": [90, 85, 89, 78]},
    {"name": "Charlie", "marks": [76, 85, 92, 80]},
    {"name": "David", "marks": [88, 78, 85, 90]},
]

# Example 16: Use lambda with map and zip to calculate the average marks for each subject
average_subject_marks = list(map(lambda subject_marks: sum(subject_marks) / len(subject_marks), zip(*[student["marks"] for student in students])))

print("\nExample 16: Average Marks for Each Subject")
print(average_subject_marks)

# Example 17: Use lambda with filter to get students with a specific pattern in their names
pattern = "a"
filtered_students = list(filter(lambda student: pattern.lower() in student["name"].lower(), students))

print("\nExample 17: Students with Names Containing 'a'")
print(filtered_students)
