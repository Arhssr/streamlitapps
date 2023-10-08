import streamlit as st
import matlab.engine
eng = matlab.engine.start_matlab()
st.title("Mathematical Operations Web App")
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
operation = st.radio("Select an operation:", ["Add", "Subtract", "Multiply", "Divide"])
if st.button("Calculate"):
    if operation == "Add":
        result = eng.plus(num1, num2)
    elif operation == "Subtract":
        result = eng.minus(num1, num2)
    elif operation == "Multiply":
        result = eng.times(num1, num2)
    elif operation == "Divide":
        if num2 != 0:
            result = eng.rdivide(num1, num2)
        else:
            result = "Cannot divide by zero"
    st.write("Result:", result)
eng.quit()
