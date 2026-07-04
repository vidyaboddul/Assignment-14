# Q10. Mini Project - Student Performance Analysis

# Import NumPy library
import numpy as np

# Generate a 2D array of shape (10, 5)
# 10 students and 5 subjects with random marks between 30 and 100
marks = np.random.randint(30, 101, (10, 5))

# Display the marks array
print("Student Marks (10 Students x 5 Subjects):")
print(marks)

# Calculate total marks of each student
total_marks = np.sum(marks, axis=1)

# Calculate average marks of each student
average_marks = np.mean(marks, axis=1)

# Display total and average marks
print("\nTotal Marks of Each Student:")
print(total_marks)

print("\nAverage Marks of Each Student:")
print(average_marks)

# Find the student with the highest total marks
highest_student = np.argmax(total_marks)

# Find the student with the lowest total marks
lowest_student = np.argmin(total_marks)

print("\nStudent with Highest Total Marks:")
print("Student Number:", highest_student + 1)
print("Total Marks:", total_marks[highest_student])

print("\nStudent with Lowest Total Marks:")
print("Student Number:", lowest_student + 1)
print("Total Marks:", total_marks[lowest_student])

# Calculate overall class mean
class_mean = np.mean(marks)

# Calculate overall class standard deviation
class_std = np.std(marks)

print("\nOverall Class Mean:", class_mean)
print("Overall Class Standard Deviation:", class_std)

# Reshape the array (Demonstration)
reshaped_marks = marks.reshape(5, 10)

print("\nReshaped Array (5 x 10):")
print(reshaped_marks)

# Find the indices of the top 3 students based on total marks
top3_indices = np.argsort(total_marks)[-3:][::-1]

# Extract marks of the top 3 students
top3_students = marks[top3_indices]

print("\nTop 3 Students (Based on Total Marks):")
print(top3_students)