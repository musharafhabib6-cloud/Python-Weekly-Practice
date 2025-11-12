import pandas as pd
import numpy as np

# Load your CSV file
data = pd.read_csv('grades.csv')

print("Original Data:\n", data)

# Calculate average marks per student
data['Average'] = data[['Math', 'Science', 'English', 'History']].mean(axis=1)

# Sort by average marks
sorted_data = data.sort_values(by='Average', ascending=False)

# Filter top students (average > 85)
top_students = sorted_data[sorted_data['Average'] > 85]

# ---- NumPy operations ----
math_scores = data['Math'].to_numpy()
science_scores = data['Science'].to_numpy()
english_scores = data['English'].to_numpy()
history_scores = data['History'].to_numpy()

# Calculate statistics
print("\n📊 Subject Statistics:")
print(f"Math → Max: {np.max(math_scores)}, Min: {np.min(math_scores)}, Std Dev: {np.std(math_scores):.2f}")
print(f"Science → Max: {np.max(science_scores)}, Min: {np.min(science_scores)}, Std Dev: {np.std(science_scores):.2f}")
print(f"English → Max: {np.max(english_scores)}, Min: {np.min(english_scores)}, Std Dev: {np.std(english_scores):.2f}")
print(f"History → Max: {np.max(history_scores)}, Min: {np.min(history_scores)}, Std Dev: {np.std(history_scores):.2f}")

# Save final data to a new file
sorted_data.to_csv('output.csv', index=False)

print("\n✅ Results saved as output.csv")
