import streamlit as st
from database import add_data


def create():
    # Layout of Create
    col1, col2 = st.columns(2)
    with col1:
        task = st.text_area("Task to do:")
    with col2:
        task_status = st.selectbox("Status", ["To do", "Executing", "Completed"])
        task_due_date = st.date_input("Due Date:")
    if st.button("Add Task"):
        add_data(task, task_status, task_due_date)
        st.success("Successfully added task: {}".format(task))
