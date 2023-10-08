import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')

st.title("Almost Desmos")
st.sidebar.header("Mathematical Function")

function_input = st.sidebar.text_input("Enter a function (e.g., 'x^3 + sin(x^2)'):")
var_name = st.sidebar.text_input("Variable name (e.g., 'x'):")
var_range = st.sidebar.slider("Variable range:", min_value=0.1, max_value=10.0, value=(0.1, 10.0), step=0.1)

st.sidebar.header("Visualization")
plot_type = st.sidebar.selectbox("Select plot type:", ["Line Plot", "Scatter Plot"])

if st.button("Generate Data and Plot"):
    try:
        expression = sp.sympify(function_input)

        x_values = np.linspace(float(var_range[0]), float(var_range[1]), 100)
        y_values = np.array([float(expression.subs(x, val)) for val in x_values])

        st.subheader("Plot:")

        if plot_type == "Line Plot":
            plt.figure(figsize=(8, 6))
            plt.plot(x_values, y_values, '-r')
            plt.xlabel(var_name)
            plt.ylabel("f(x)")
            plt.title("Line Plot")
            st.pyplot(plt)
        elif plot_type == "Scatter Plot":
            plt.figure(figsize=(8, 6))
            plt.scatter(x_values, y_values, c='blue', marker='o', s=10)
            plt.xlabel(var_name)
            plt.ylabel("f(x)")
            plt.title("Scatter Plot")
            st.pyplot(plt)

    except Exception as e:
        st.error(f"Error: {str(e)}")
