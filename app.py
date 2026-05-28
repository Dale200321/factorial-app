import streamlit as st
from factorial import fact
import os

def load_user():
     # Đọc danh sách user từ file user.txt
    try:
        if os.path.exists("user.txt"):
            with open("user.txt", "r", encoding = "utf-8") as f:
                users = [line.strip() for line in f.readlines() if line.strip()]
            return users
        else:
            st.error("file user.txt does not exist")
            return []
    except Exception as e:
        st.error(f"Error when reading file user.txt: {e}")
        return []

def login_page():
    st.title("Login"):

    username = st.text_input("Enter username:")

    if st.button("Login"):
        if username:
            users = load_users()
            if username in users:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.session_state.show_greeting = True
                st.session_state.username = username
                st.rerun()
        else:
            st.warning("Please enter username!")

def factorial_calculator():
    st.title("Factorial Calculator")

    st.write(f"Hello, {st.ssession_state.username}!")

    if st.button("Log out"):
        st.session_state.logged_in = False
        st.session_state.username = " "
        st. rerun

    st.divider()
    
    number = st.number_input("Enter a number:",
                             min_value=0,
                             max_value=900)
    if st.button("Calculate"):
        result = fact(number)
        st.write(f'The factorial of {number} is {result}')

def greeting_page():
    st.title("Hola!")
    st.write(f"Hello {st.session_state.username}")
    st.write("You have no permission to proceed")

if st.button("Return to login"):
    st.session_state.show_greeting = False
    st.session_state.username = " "
    st.rerun()

def main():
     if 'logged_in' not in st.session_state:
          st.session_state.logged_in = False
     if 'username' not in st.session_state:
          st.session_state.username = ''
     if 'show_greeting' not in st.session_state:
          st.session_state.show_greeting = False

     if st.session_state.logged_in:
          factorial_calculator()
     elif st.session_state.show_greeting:
          greeting_page()
     else:
          login_page()
        
if __name__ == "__main__":
    main()

