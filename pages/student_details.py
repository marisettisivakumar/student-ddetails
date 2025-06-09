import streamlit as st
from models.student_model import get_student_by_id

st.title("🔍 View Student Details")

student_id = st.text_input("Enter Student ID")

if st.button("Search"):
    data = get_student_by_id(student_id)
    if data:
        st.subheader("👤 Student Profile")
        st.json(data)
    else:
        st.warning("Student not found.")
