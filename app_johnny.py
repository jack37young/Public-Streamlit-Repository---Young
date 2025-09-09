import streamlit as st

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to switch page
def go_to_page(page_name):
    st.session_state.page = page_name



# Page 1: Home page with "Blueberry" button
if st.session_state.page == "home":
    st.title("Welcome!")
    if st.button("Blueberry):
        go_to_page("blueberry)
    

# Page 2: Number input page
elif st.session_state.page == "blueberry":
    st.title("Blueberry)
    
    # Number input
    number = st.number_input("Enter a number:", value=0)
    
    if st.button("Submit"):
        # Write the number to a text file
        with open("numbers.txt", "a") as file:
            file.write(f"{number}\n")
        st.success(f"Number {number} saved!")
    
    # Back button to go to home page
    if st.button("Back"):
        go_to_page("home")







