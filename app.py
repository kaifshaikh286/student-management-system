import streamlit as st
import sqlite3
import pandas as pd

# Database Connection
conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

st.title("🎓 Student Management System")

menu = ["Add Student", "View Students", "Search Student", "Update Student", "Delete Student"]

choice = st.sidebar.selectbox("Menu", menu)

# Add Student
if choice == "Add Student":
    st.subheader("Add New Student")

    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=1, max_value=100)
    course = st.text_input("Enter Course")

    if st.button("Add Student"):
        cursor.execute(
            "INSERT INTO students(name, age, course) VALUES (?, ?, ?)",
            (name, age, course)
        )
        conn.commit()
        st.success("Student Added Successfully")

# View Students
elif choice == "View Students":
    st.subheader("All Students")

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    df = pd.DataFrame(data, columns=["ID", "Name", "Age", "Course"])

    st.dataframe(df)

# Search Student
elif choice == "Search Student":
    st.subheader("Search Student")

    search_name = st.text_input("Enter Student Name")

    if st.button("Search"):
        cursor.execute(
            "SELECT * FROM students WHERE name=?",
            (search_name,)
        )

        data = cursor.fetchall()

        df = pd.DataFrame(data, columns=["ID", "Name", "Age", "Course"])

        st.dataframe(df)

# Update Student
elif choice == "Update Student":
    st.subheader("Update Student")

    student_id = st.number_input("Enter Student ID", min_value=1)

    new_name = st.text_input("New Name")
    new_age = st.number_input("New Age", min_value=1, max_value=100)
    new_course = st.text_input("New Course")

    if st.button("Update"):
        cursor.execute("""
        UPDATE students
        SET name=?, age=?, course=?
        WHERE id=?
        """, (new_name, new_age, new_course, student_id))

        conn.commit()

        st.success("Student Updated Successfully")

# Delete Student
elif choice == "Delete Student":
    st.subheader("Delete Student")

    student_id = st.number_input("Enter Student ID to Delete", min_value=1)

    if st.button("Delete"):
        cursor.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )

        conn.commit()

        st.success("Student Deleted Successfully")