import streamlit as st

st.title("Standalone Calculator")
number1 = st.number_input(label="Enter first number")
number2 = st.number_input(label="Enter second number")
st.write("Operation")
operation = st.radio("Select an operation to perform:", ("+‎", "‎-", "×", "÷"))
result = 0

def calculate():
    try:
        if operation == "+‎":
            result = number1 + number2
        elif operation == "‎-":
            result = number1 - number2
        elif operation == "×":
            result = number1 * number2
        elif operation == "÷" and number2 != 0:
            result = number1 / number2
        else:
            st.warning("Division by 0 error. Please enter a non-zero number.")
            return
        st.success(f"Result = {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if st.button("Calculate"):
    calculate()
