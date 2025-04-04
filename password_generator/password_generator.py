import streamlit as st
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers,  use_special):
    """Generate a random password based on the specified criteria."""
    
    characters = string.ascii_letters

    if length < 8:
        st.error("Password length should be at least 8 characters.")
        return None
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if not characters:
        st.error("At least one character type must be selected.")
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

st.title("Password Generator")
st.write("Generate a secure password based on your preferences.")

# Sidebar for user input
st.sidebar.header("Password Criteria")
length = st.sidebar.slider("Password Length", min_value=8, max_value=32, value=12)
use_uppercase = st.sidebar.checkbox("Include Uppercase Letters", value=True)
use_lowercase = st.sidebar.checkbox("Include Lowercase Letters", value=True)
use_numbers = st.sidebar.checkbox("Include Numbers", value=True)
use_special = st.sidebar.checkbox("Include Special Characters", value=True)

# Generate password button
if st.sidebar.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
    if password:
        st.success(f"Generated Password: {password}")
        st.code(password)
    else:
        st.error("Failed to generate password. Please check your criteria.")

