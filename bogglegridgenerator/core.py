#Copy-pasted example app logic
import random
import numpy as np
from constants import SUPPORTED_LANGUAGES
import streamlit as st


def generate_grid(language_name: str, grid_size: int = 4):
    lang_data = SUPPORTED_LANGUAGES[language_name]
    letters = lang_data["letters"]
    weights = lang_data["weights"]

    grid_letters = random.choices(letters, weights, k = grid_size * grid_size)
    return [grid_letters[i : i+grid_size] for i in range(0, len(grid_letters), grid_size)]




def minimal_letter_grid(grid):
    html = "<table style='border-collapse: separate; border-spacing: 5px;'>"
    for row in grid:
        html += "<tr>"
        for cell in row:
            html += f"<td style='padding: 20px; text-align: center; font-size: 28px; font-weight: bold; width: 80px;'>{cell}</td>"
        html += "</tr>"
    html += "</table>"
    st.markdown(html, unsafe_allow_html=True)