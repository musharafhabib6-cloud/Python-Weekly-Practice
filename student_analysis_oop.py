import pandas as pd
import numpy as np

# ---- Student Class ----
class Student:
    def __init__(self, name, math, science, english, history):
        self.name = name
        self.math = math
        self.science = science
        self.english = english
        self.history = history
        self.average = self.calculate_average()
        self.grade = self.assign_grade()

    def calculate_average(self):
        return (self.math + self.science + self.english + self.history) / 4

    def assign_grade(self):
        if self.average >= 90:
            return 'A'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'

# ---- Load CSV Data ----
data = pd.read_csv('grades.csv')

# ---- Create Student objects ----
students = [
    Student(row['Name'], row['Math'], row['Science'], row['English'], row['History'])
    for _, row in data.iterrows()
]

# ---- Create DataFrame from objects ----
processed_data = pd.DataFrame([{
    'Name': s.name,
    'Math': s.math,
    'Science': s.science,
    'English': s.english,
    'History': s.history,
    'Average': round(s.average, 2),
    'Grade': s.grade
} for s in students])

# ---- NumPy statistics ----
print("\n📊 Subject Statistics:")
for subject in ['Math', 'Science', 'English', 'History']:
    scores = processed_data[subject].to_numpy()
    print(f"{subject} → Max: {np.max(scores)}, Min: {np.min(scores)}, Std Dev: {np.std(scores):.2f}")

# ---- Sort by average and save to CSV ----
processed_data = processed_data.sort_values(by='Average', ascending=False)
processed_data.to_csv('output.csv', index=False)

print("\n✅ Processed data saved to output.csv")
print("\nTop Students:\n", processed_data.head())
