#Copy-pasted example app.py for Streamlit app
import streamlit as st
from gridgenerator.core import generate_grid

st.set_page_config(page_title="GridGenerator", layout="wide")

st.title("🧩 Grid Generator Tool")

rows = st.number_input("Rows", min_value=1, value=5)
cols = st.number_input("Columns", min_value=1, value=5)
generate_button = st.button("Generate Grid")

if generate_button:
    grid = generate_grid(rows, cols)
    st.write(grid)
