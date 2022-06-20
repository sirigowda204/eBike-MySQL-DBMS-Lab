# Importing pakages
import streamlit as st

from create import create
from database import create_table, add_data, view_all_data, view_only_tasks, get_task, edit_task_data, delete_data
from delete import delete
from read import read
from update import update


def main():
    st.title("Scheduler App")
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Add":
        st.subheader("Create a task:")
        create()

    elif choice == "View":
        st.subheader("View created tasks")
        read()

    elif choice == "Edit":
        st.subheader("Update created tasks")
        update()

    elif choice == "Remove":
        st.subheader("Delete created tasks")
        delete()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
