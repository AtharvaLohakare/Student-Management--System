# 🎓 Student Management System (Python)

A simple command-line Student Management System built using Python. This project allows users to manage student records with JSON file storage and CSV import/export support.

---

## 📌 Features

- ➕ Add Student
- 📋 Display All Students
- 🔍 Search Student (by Roll Number or Name)
- ✏️ Update Student Details
- ❌ Delete Student
- 🔢 Count Total Students
- 📊 Sort Students
  - By Name
  - By Age
  - By Roll Number
- 💾 Save Data in JSON
- 📂 Load Data from JSON
- 📤 Export Student Data to CSV
- 📥 Import Student Data from CSV
- ⚠️ Exception Handling

---

## 🛠️ Technologies Used

- Python 3
- JSON Module
- CSV Module
- Object-Oriented Programming (OOP)

---

## 📁 Project Structure

```
Student-Management-System/
│
├── main.py              # Main program
├── operations.py        # All student operations
├── student.py           # Student class
├── students.json        # Student database
├── students.csv         # CSV export/import
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository

```
git clone https://github.com/yourusername/Student-Management-System.git
```

2. Open the project folder.

3. Run

```
python main.py
```

---

## 📋 Menu

```
1. Add Student
2. Display All Students
3. Delete Student
4. Search Student
5. Update Student
6. Count Students
7. Sort Students
8. Export to CSV
9. Import from CSV
10. Exit
```

---

## 💾 JSON Storage

Student records are stored in `students.json`.

Example:

```json
[
    {
        "name": "Atharva",
        "roll": 34,
        "age": 21
    },
    {
        "name": "Rahul",
        "roll": 12,
        "age": 20
    }
]
```

---

## 📄 CSV Export

Example:

```csv
Name,Roll,Age
Atharva,34,21
Rahul,12,20
```

---

## ⚠ Exception Handling

This project handles:

- Invalid Input (`ValueError`)
- Missing JSON File (`FileNotFoundError`)
- Corrupted JSON File (`JSONDecodeError`)
- Duplicate Roll Numbers
- Invalid CSV Data

---

## 🧠 Concepts Used

- Functions
- Classes & Objects
- File Handling
- JSON
- CSV
- Exception Handling
- Loops
- Lists
- Sorting
- Lambda Functions
- Enumerate
- String Formatting
- Modular Programming

---

## 🚀 Future Improvements

- Login System
- Password Protection
- Export to Excel (.xlsx)
- Student Marks Management
- Attendance Management
- GUI using Tkinter
- Database (SQLite/MySQL)
- Search by Multiple Fields
- Filter Students
- Pagination
- Statistics Dashboard

---

## 👨‍💻 Author

**Atharva Vasant Lohakare**

Python Developer | Learning AI & ML | Open Source Enthusiast

GitHub: *(Add your GitHub profile here)*

LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ Version

**Student Management System v2.0**

---

If you found this project helpful, don't forget to ⭐ the repository.
