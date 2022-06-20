import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data


def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Task', 'Status', 'Due Date'])
    with st.expander("View all tasks"):
        st.dataframe(df)
    with st.expander("Task Status"):
        task_df = df['Status'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)
        p1 = px.pie(task_df, names='index', values='Status')
        st.plotly_chart(p1)