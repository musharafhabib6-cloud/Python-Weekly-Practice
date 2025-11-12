import pandas as pd
import numpy as np

# -----------------------------
# Student Class
# -----------------------------
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
        return round((self.math + self.science + self.english + self.history) / 4, 2)

    def assign_grade(self):
        avg = self.average
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

# -----------------------------
# Load Dataset
# -----------------------------
print("📂 Loading dataset...")
data = pd.read_csv('grades.csv')

# -----------------------------
# Create Student Objects
# -----------------------------
students = [Student(row['Name'], row['Math'], row['Science'], row['English'], row['History'])
            for _, row in data.iterrows()]

# -----------------------------
# Convert to DataFrame
# -----------------------------
processed_data = pd.DataFrame([{
    'Name': s.name,
    'Math': s.math,
    'Science': s.science,
    'English': s.english,
    'History': s.history,
    'Average': s.average,
    'Grade': s.grade
} for s in students])

# -----------------------------
# Subject Statistics (NumPy)
# -----------------------------
print("\n📊 Subject Statistics:")
for subject in ['Math', 'Science', 'English', 'History']:
    scores = processed_data[subject].to_numpy()
    print(f"{subject} → Max: {np.max(scores)}, Min: {np.min(scores)}, Mean: {np.mean(scores):.2f}, Std Dev: {np.std(scores):.2f}")

# -----------------------------
# Save Final Results
# -----------------------------
processed_data = processed_data.sort_values(by='Average', ascending=False)
processed_data.to_csv('output2.csv', index=False)

print("\n✅ Analysis complete! Results saved to output2.csv")
print("\n🏆 Top 3 Students:\n", processed_data.head(3))
