#Defining function to create an input page for each flavor and write it into a file

import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to_page(page_name):
    st.session_state.page = page_name


def open_page(type):
    global flavor
    st.title(type)
    date = st.date_input("Date: ")
    number = st.number_input("{type} Sold")
    if st.button("Submit"):
        with open("numbers.txt", "a") as file:
            file.write(f"{date}: {number}\n")
        st.success(f"Saved")
    if st.button("Back"):
        go_to_page("home")


if st.session_state.page == "home":
    st.title("Welcome!")
    if st.button("Blue Raspberry"):
        flavor = "Blue Raspberry"
        open_page(flavor)
    elif st.button("Tiger Blood"):
        flavor = "Tiger Bloode"
        open_page(flavor)
    elif st.button("Banana"):
        flavor = "Banana"
        open_page(flavor)
    elif st.button("Wedding Cake"):
        flavor = "Wedding Cake"
        open_page(flavor)
    elif st.button("Strawberry Lemonade"):
        flavor = "Strawberry Lemonade"
        open_page(flavor)
    elif st.button("Sour Apple"):
        flavor = "Sour Apple"
        open_page(flavor)
    elif st.button("Cotton Candy"):
        flavor = "Cotton Candy"
        open_page(flavor)
    elif st.button("Arctic Blast"):
        flavor = "Arctic Blast"
        open_page(flavor)











