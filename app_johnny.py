import streamlit as st
import pandas as pd
import os 
from datetime import date

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to switch page
def go_to_page(page_name):
    st.session_state.page = page_name


flavors = [
    "Blue Raspberry",
    "Tiger Blood",
    "Banana",
    "Wedding Cake",
    "Strawberry Lemonade",
    "Sour Apple",
    "Cotton Candy",
    "Arctic Blast"
]



    
if st.session_state.page == "home":
    st.title("Welcome! Select a flavor from the dropdown above to enter sales.")
    selected_page = st.selectbox("Choose a flavor:", flavors)
    st.session_state.page = selected_page

#Blue Raspberry Page
if st.session_state.page == "blue_razz":
    st.title("Blue Raspberry")
    
    # Number input
    date = st.date_input("Date:")
    number = st.number_input("How many cups sold: ", value=0)
    
    if st.button("Submit"):
        # Write the number to a text file
        with open("numbers.txt", "a") as file:
            file.write(f"{date} Blue Raspberry {number}\n")
        st.success(f"Number {number} saved!")
    
    # Back button to go to home page
    if st.button("Back"):
        go_to_page("home")


#Tiger Blood Page
if st.session_state.page == "tiger_blood":
    st.title("Tiger Blood")
    
    # Number input
    date = st.date_input("Date:")
    number = st.number_input("How many cups sold: ", value=0)
    
    if st.button("Submit"):
        # Write the number to a text file
        with open("numbers.txt", "a") as file:
            file.write(f"{date} Tiger Blood {number}\n")
        st.success(f"Number {number} saved!")
    
    # Back button to go to home page
    if st.button("Back"):
        go_to_page("home")


#Banana Page
if st.session_state.page == "banana":
    st.title("Banana")
    
    # Number input
    date = st.date_input("Date:")
    number = st.number_input("How many cups sold: ", value=0)
    
    if st.button("Submit"):
        # Write the number to a text file
        with open("numbers.txt", "a") as file:
            file.write(f"{date} Banana {number}\n")
        st.success(f"Number {number} saved!")
    
    # Back button to go to home page
    if st.button("Back"):
        go_to_page("home")



#Wedding Cake Page
if st.session_state.page == "wedding_cake":
    st.title("Wedding Cake")
    
    # Number input
    date = st.date_input("Date:")
    number = st.number_input("How many cups sold: ", value=0)
    
    if st.button("Submit"):
        # Write the number to a text file
        with open("numbers.txt", "a") as file:
            file.write(f"{date} Wedding Cake {number}\n")
        st.success(f"Number {number} saved!")
    
    # Back button to go to home page
    if st.button("Back"):
        go_to_page("home")


#Strawberry Lemonade Page
if st.session_state.page == "straw_lem":
    st.title("Strawberry Lemonade")
    
    # Number input
    date = st.date_input("Date:")
    number = st.number_input("How many cups sold: ", value=0)
    
    if st.button("Submit"):
        # Write the number to a text file
        with open("numbers.txt", "a") as file:
            file.write(f"{date} Strawberry Lemonade {number}\n")
        st.success(f"Number {number} saved!")
    
    # Back button to go to home page
    if st.button("Back"):
        go_to_page("home")


#Sour Apple Page
if st.session_state.page == "sour_apple":
    st.title("Sour Apple")
    
    # Number input
    date = st.date_input("Date:")
    number = st.number_input("How many cups sold: ", value=0)
    
    if st.button("Submit"):
        # Write the number to a text file
        with open("numbers.txt", "a") as file:
            file.write(f"{date} Sour Apple {number}\n")
        st.success(f"Number {number} saved!")
    
    # Back button to go to home page
    if st.button("Back"):
        go_to_page("home")


#Cotton Candy Page
if st.session_state.page == "cotton_candy":
    st.title("Cotton Candy")
    
    # Number input
    date = st.date_input("Date:")
    number = st.number_input("How many cups sold: ", value=0)
    
    if st.button("Submit"):
        # Write the number to a text file
        with open("numbers.txt", "a") as file:
            file.write(f"{date} Cotton Candy {number}\n")
        st.success(f"Number {number} saved!")
    
    # Back button to go to home page
    if st.button("Back"):
        go_to_page("home")



#Arctic Blast Page
if st.session_state.page == "arctic_blast":
    st.title("Arctic Blast")
    
    # Number input
    date = st.date_input("Date:")
    number = st.number_input("How many cups sold: ", value=0)
    
    if st.button("Submit"):
        # Write the number to a text file
        with open("numbers.txt", "a") as file:
            file.write(f"{date} Arctic Blast {number}\n")
        st.success(f"Number {number} saved!")
    
    # Back button to go to home page
    if st.button("Back"):
        go_to_page("home")













