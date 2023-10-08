import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
st.title("Whiteboard/Canvas")
canvas = st_canvas(
    fill_color="rgba(255, 160, 0, 0.3)",
    stroke_width=5,
    stroke_color="black",
    background_color="#eee",
    width=800,
    height=800,
    drawing_mode="freedraw",
    key="canvas",)
if st.button("Clear Canvas"):
    canvas.json_data = []
st.json(canvas.json_data)
