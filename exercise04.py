import numpy as np
import pandas as pd
import streamlit as st

# Exercise 5: Filtering DataFrames with Widgets

# Goal: Filter a Pandas DataFrame based on user selections from widgets.
# Use a selectbox to filter by category and a slider to filter by a numerical value.

st.title("Exercise 5: Interactive Data Filtering")


# Generate sample data
@st.cache_data
def load_data():
    data = pd.DataFrame(
        {
            "value": np.random.rand(200) * 100,
            "category": np.random.choice(["Apple", "Banana", "Cherry"], 200),
        }
    )
    return data


df = load_data()

st.subheader("Original Data")
st.dataframe(df.head(), use_container_width=True)

# --- Your code starts here ---

# TODO: Create a selectbox to choose a category.
# Label it "Select Category". Options should be the unique categories from the 'category' column.
# Add an "All" option to show all categories.


# TODO: Create a slider to select a range for the 'value' column.
# Label it "Select Value Range".
# The min and max should be the min and max of the 'value' column.
# The default value should be the full range.


# TODO: Filter the DataFrame `df` based on the selected category.
# If "All" is selected, don't filter by category.


# TODO: Further filter the DataFrame based on the selected value range from the slider.
# The filtered DataFrame should be stored in a variable, e.g., `filtered_df`.

filtered_df = df  # Replace this with your filtered dataframe

# --- Your code ends here ---

st.subheader("Filtered Data")
# Display the filtered data
st.write(f"Showing {len(filtered_df)} records")
st.dataframe(filtered_df, use_container_width=True)

# To run: streamlit run exercise04.py
