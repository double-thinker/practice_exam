import pandas as pd
import streamlit as st

# Exercise 3: Streamlit Forms and Callbacks

# Goal: Create a form to collect user information (name, email) and add it to a list
# stored in session state when the form is submitted. Use a callback function for submission.

st.title("Exercise 3: User Registration Form")

# Initialize the list of users in session state if it doesn't exist
if "user_list" not in st.session_state:
    st.session_state.user_list = []

# --- Your code starts here ---

# TODO: Define a callback function `add_user`.
# This function should append a dictionary containing the current 'user_name' and 'user_email'
# from session state to the `st.session_state.user_list`.
# Hint: Access form input values via session state using their keys.


# TODO: Create a Streamlit form using `st.form`.

# TODO: Inside the form, create a text input for 'Name' with the key 'user_name'.

# TODO: Inside the form, create a text input for 'Email' with the key 'user_email'.

# TODO: Inside the form, create a submit button using `st.form_submit_button`.
# Label it "Register" and set its `on_click` parameter to your `add_user` callback function.

# --- Your code ends here ---

st.subheader("Registered Users:")
# Display the list of registered users
if st.session_state.user_list:
    st.table(pd.DataFrame(st.session_state.user_list))
else:
    st.write("No users registered yet.")

# To run: streamlit run exercise03.py
