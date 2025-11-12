# 🐍 Weekly Python Practice Project

This repository contains my weekly Python practice work — covering environment setup, debugging, Python basics, data handling, object-oriented programming, and version control with Git and GitHub.

---

## 📌 Project Overview

This project includes:

- Python scripts for practicing variables, loops, lists, functions, and object-oriented programming (OOP).
- Handling real-world structured data using CSV files with **NumPy** and **Pandas**.
- Generating Word reports (`.docx`) and PowerPoint presentations (`.pptx`) programmatically.
- Applying debugging, code organization, and PEP8 code style.
- Version control practice using **Git** and **GitHub**.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```
git clone https://github.com/yourusername/YourProjectName.git
cd YourProjectName
```

### 2️⃣ Create and Activate Conda Environment
```
conda create -n myenv python=3.11
conda activate myenv
```

### 3️⃣ Install Required Libraries
```
pip install -r requirements.txt
```

**Dependencies in `requirements.txt`:**
- pandas
- numpy
- python-docx
- python-pptx
- flake8

---

## ▶️ How to Run the Scripts

### 1. Analyze Grades
```
python analyze_grades.py
```
- Reads `grades.csv`
- Calculates average, highest, and lowest marks
- Filters students above average
- Saves filtered results to `output.csv`

### 2. Generate Word Report
```
python weekly_python_report.py
```
- Creates a Word report file: `Weekly_Python_Practice_Report.docx`

### 3. Generate Presentation
```
python weekly_presentation.py
```
- Creates a PowerPoint presentation: `Weekly_Python_Practice_Presentation.pptx`

---

## 📁 Project Structure

```
project/
│
├─ src/                  # Python scripts
│   ├─ analyze_grades.py
│   ├─ final_project.py
│   ├─ student_analysis_oop.py
│   ├─ weekly_python_report.py
│   └─ weekly_presentation.py
│
├─ data/                 # CSV input files
│   └─ grades.csv
│
├─ output/               # Generated outputs
│   ├─ output.csv
│   ├─ Weekly_Python_Practice_Report.docx
│   └─ Weekly_Python_Practice_Presentation.pptx
│
├─ README.md             # Project documentation
└─ requirements.txt      # Python dependencies
```

---

## 🧠 Topics Covered

- Conda environment setup
- IDE integration (VS Code / PyCharm)
- Debugging practice
- Python basics: variables, loops, lists, functions
- NumPy & Pandas for data handling
- Object-oriented programming (classes and methods)
- Mini-project: CSV data analysis
- Git & GitHub version control
- PEP8 code style with flake8

---

## 💡 Author

**Name:** ___________________________
*(You can add your name here)*

---

## 🧾 License

This project is open-source and free to use for educational purposes.

