#Copy-pasted example app.py for Streamlit app
import streamlit as st
from bogglegridgenerator.core import generate_grid
from bogglegridgenerator.core import minimal_letter_grid
from constants import SUPPORTED_LANGUAGES

st.set_page_config(page_title="GridGenerator", layout="wide")

st.title("🧩 Grid Generator Tool")

selectedLanguage = st.selectbox("Choose a language", list(SUPPORTED_LANGUAGES.keys()))
selectedSize = st.slider("Select the dimensions of your grid (4x4 etc.", min_value=2, max_value=10, value=4)
customWeights = st.toggle("Use custom weights")
generate_button = st.button("Generate Grid")

if generate_button:
    grid = generate_grid(selectedLanguage, selectedSize)
    minimal_letter_grid(grid)
