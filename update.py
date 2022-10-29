import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_tasks, get_task, edit_task_data


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Task', 'Status', 'Due Date'])
    with st.expander("Current tasks"):
        st.dataframe(df)
    list_of_tasks = [i[0] for i in view_only_tasks()]
    selected_task = st.selectbox("Task to Edit", list_of_tasks)
    selected_result = get_task(selected_task)
    # st.write(selected_result)
    if selected_result:
        task = selected_result[0][0]
        task_status = selected_result[0][1]
        task_due_date = selected_result[0][2]

        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_task = st.text_area("Task to do:", task)
        with col2:
            new_task_status = st.selectbox(task_status, ["To do", "Executing", "Completed"])
            new_task_due_date = st.date_input('Due Date', task_due_date)
        if st.button("Update Task"):
            edit_task_data(new_task, new_task_status, new_task_due_date, task, task_status, task_due_date)
            st.success("Successfully updated:: {} to ::{}".format(task, new_task))
    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Task', 'Status', 'Due Date'])
    with st.expander("Updated data"):
        st.dataframe(df2)
