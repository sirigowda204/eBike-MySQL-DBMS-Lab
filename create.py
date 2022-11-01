import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        dealer_id = st.text_input("ID:")
        dealer_name = st.text_input("Name:")
    with col2:
        dealer_city = st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])
        dealer_pin = st.text_input("Pin Code:")
    dealer_street = st.text_input("Street Name:")
    if st.button("Add Dealer"):
        add_data(dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street)
        st.success("Successfully added Dealer: {}".format(dealer_name))
