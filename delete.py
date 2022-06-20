import pandas as pd
import streamlit as st
from database import view_all_data, view_only_tasks, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Task', 'Status', 'Due Date'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_tasks = [i[0] for i in view_only_tasks()]
    selected_task = st.selectbox("Task to Delete", list_of_tasks)
    st.warning("Do you want to delete ::{}".format(selected_task))
    if st.button("Delete Task"):
        delete_data(selected_task)
        st.success("Task has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Task', 'Status', 'Due Date'])
    with st.expander("Updated data"):
        st.dataframe(df2)