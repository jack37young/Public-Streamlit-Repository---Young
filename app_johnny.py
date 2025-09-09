
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
        # Write the data to a text file. Note: This will not be persistent on Streamlit Cloud.
        # For a production app, you would use a database or a cloud storage service.
        with open("sales_data.txt", "a") as file:
            file.write(f"{selected_date},{flavor_name},{number}\n")
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







