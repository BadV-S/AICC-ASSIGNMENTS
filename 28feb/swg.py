# ----------------------------------------
# Storytelling with Graphs
# ----------------------------------------

import matplotlib.pyplot as plt

# Sample dataset
subjects = ['Math', 'Science', 'English', 'History', 'Computer']
marks = [85, 78, 90, 65, 92]

# -----------------------------
# Bar Chart
# -----------------------------
plt.figure()
plt.bar(subjects, marks)
plt.title("Marks in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# -----------------------------
# Pie Chart
# -----------------------------
plt.figure()
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Marks Distribution by Subject")
plt.show()

# -----------------------------
# Histogram
# -----------------------------
student_marks = [85, 78, 90, 65, 92, 88, 75, 70, 95, 82, 67, 73]

plt.figure()
plt.hist(student_marks, bins=5)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()