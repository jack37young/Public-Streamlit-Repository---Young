
import streamlit as st
import pandas as pd
import os 
from datetime import date

excel_file = "johnny_freeze_sales.xlsx"

# Page Navigation Functions
def go_to_page(page_name):
    st.session_state.page = page_name

def flavor_page(flavor_name):
    st.title(flavor_name)

    #Number and Date inputs
    current_date = date.today()
    selected_date = st.date_input("Date:", value=current_date)
    
    number = st.number_input(f"How many cups of {flavor_name} sold:", min_value=0, value=0)
    
    if st.button("Submit Sales"):
        try:
            # Read the existing Excel file into a DataFrame
            # The first column is designated to the dates
            df = pd.read_excel(excel_file, index_col=0)
        except FileNotFoundError:
            # Error Checking in case file does not exist
            df = pd.DataFrame()
            # Fill any missing values with 0
        df = df.fillna(0)
        
        # Make sure the date is in the correct Datetime
        df.index = pd.to_datetime(df.index)
        
        # Convert the selected date to a datetime object
        selected_date_dt = pd.to_datetime(selected_date)

        # Get the current value, defaulting to 0 if the cell is empty or doesn't exist
        current_sales = df.at[selected_date_dt, flavor_name] if selected_date_dt in df.index and flavor_name in df.columns else 0

        # Update the DataFrame with the new sales data, creates a new row if date does not yet exist
        # The .at method is used for fast scalar access
        df.at[selected_date_dt, flavor_name] = current_sales + number
        df.to_excel(excel_file, index=True)
        st.success(f"Successfully saved {number} cups of {flavor_name} sales for {selected_date}!")

        
    # Button to go back to the home page
    if st.button("Back to Home"):
        go_to_page("home")

# Initialize Session State
if "page" not in st.session_state:
    st.session_state.page = "home"
    
# Flavors
flavors = [
    "-",
    "Blue Raspberry",
    "Tiger Blood",
    "Banana",
    "Wedding Cake",
    "Strawberry Lemonade",
    "Sour Apple",
    "Cotton Candy",
    "Arctic Blast"
]

# Flavor and Page Dictionary
flavor_page_map = {
    "Blue Raspberry": "blue_razz",
    "Tiger Blood": "tiger_blood",
    "Banana": "banana",
    "Wedding Cake": "wedding_cake",
    "Strawberry Lemonade": "straw_lem",
    "Sour Apple": "sour_apple",
    "Cotton Candy": "cotton_candy",
    "Arctic Blast": "arctic_blast"
}

# Main App

# Home Page
if st.session_state.page == "home":
    st.title("Johnny Freeze Sales Inputs")
    st.write("Select a flavor to enter its daily sales data.")
    
    selected_flavor = st.selectbox("Choose a flavor:", flavors)
    
    if selected_flavor != "-":
        if st.button(f"Go to {selected_flavor}"):
            page_id = flavor_page_map[selected_flavor]
            go_to_page(page_id)

# Flavor Pages
elif st.session_state.page in flavor_page_map.values():
    current_flavor = next(key for key, value in flavor_page_map.items() if value == st.session_state.page)
    flavor_page(current_flavor)







