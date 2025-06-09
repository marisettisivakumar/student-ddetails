import streamlit as st
from models.student_model import add_student
from datetime import date

st.title("📝 Student Enrollment Form")

with st.form("enroll_form"):
    student_id = st.text_input("Student ID")
    name = st.text_input("Name")
    dob = st.date_input("Date of Birth", date(2000, 1, 1))
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    class_ = st.text_input("Class")
    section = st.text_input("Section")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    address = st.text_area("Address")

    submit = st.form_submit_button("Enroll Student")

    if submit:
        data = (student_id, name, dob, gender, class_, section, phone, email, address)
        add_student(data)
        st.success(f"Student {name} enrolled successfully!")
