import streamlit as st

# Exercise 1: Basic Streamlit Layout

# Goal: Arrange the following widgets into two columns.
# The first column should contain the text input and the button.
# The second column should contain the slider and the checkbox.

st.title("Exercise 1: Streamlit Layout")

# --- Your code starts here ---

# TODO: Create two columns using st.columns()

# TODO: Place the text input and button in the first column using a 'with' block

# TODO: Place the slider and checkbox in the second column using a 'with' block


# --- Your code ends here ---

# Display the results (this part should remain outside the columns)
st.write(f"Name: {name}")
if button_clicked:
    st.write("Button was clicked!")

st.write(f"Age: {age}")

# To run: streamlit run exercise01.py
