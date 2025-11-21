import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import json
import os

# --- FIX 1: Page Config must be the first Streamlit command ---
st.set_page_config(layout="wide", page_title="Climate Vulnerability Index Table")

st.title("Climate Vulnerability Index Table")
st.markdown("*Inside the Lab: Decoding the Climate Vulnerability Index!*")

hide_streamlit_style = """
    <style>
    /* Hide header and hamburger menu */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://encycolorpedia.com/d2e8ba.png");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

sidebar_bg = """
<style>
[data-testid="stSidebar"] {
    background-image: url("https://www.dictionary.com/e/wp-content/uploads/2016/01/hunter-green-color-paint-code-swatch-chart-rgb-html-hex.png");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}
</style>
"""
st.markdown(sidebar_bg, unsafe_allow_html=True)

# --- FIX 2: Robust Path Handling for Logo ---
try:
    # Get the directory where this script is located (pages folder)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the root directory
    parent_dir = os.path.dirname(current_dir)
    # Construct the full path to the image
    logo_path = os.path.join(parent_dir, "klimata_logo.png")
    
    st.sidebar.image(logo_path, use_column_width=True)
except Exception as e:
    st.sidebar.error("Logo not found. Please check the file path.")

st.markdown("""
<style>

/* --- Make sidebar text white --- */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* --- Make navigation tab text white --- */
[data-testid="stNavigation"] div[data-testid="stSidebarNav"] * {
    color: white !important;
}

/* Optional: Make sidebar background dark for contrast */
[data-testid="stSidebar"] {
    background-color: #0D0D0D !important;
}

</style>
""", unsafe_allow_html=True)

# --- Potential Fix for CSV ---
# If RISK_TABLE.csv is also in the root folder, you might need to use parent_dir for it too.
# For now, we keep it as is, but wrapped in a try-except to be safe.
try:
    df = pd.read_csv("RISK_TABLE.csv")
    
    # Style DataFrame with Pandas Styler
    styled_df = (
        df.style
          .set_table_styles([
              {'selector': 'thead',
               'props': [
                   ('background-color', '#D2E8BA'),
                   ('color', 'black'),
                   ('font-weight', 'bold'),
                   ('border', '1px solid black')
               ]},
              {'selector': 'td',
               'props': [
                   ('border', '1px solid black'),
                   ('padding', '8px')
               ]},
              {'selector': 'table',
               'props': [
                   ('border-collapse', 'collapse'),
                   ('table-layout', 'fixed'),
                   ('text-align', 'center')
               ]}
          ])
    )

    # Render in a container that fits the table width exactly
    st.markdown(
        f"""
        <div style="
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            display: inline-block;   /* container shrinks to table width */
            max-height: 500px;
            overflow: auto;
        ">
            {styled_df.to_html(render_links=True, escape=False)}
        </div>

        <style>
            table {{
                width: auto;           /* table width adapts to content */
                table-layout: fixed;   /* evenly stretch columns */
            }}
            th, td {{
                text-align: center;
                word-wrap: break-word;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
except FileNotFoundError:
    st.error("⚠️ Could not find 'RISK_TABLE.csv'. Please ensure the file is uploaded to the repository.")

st.markdown("### Access the Iloilo City Datasets here!")

# Links to your dataset folders
link1 = "https://drive.google.com/drive/folders/1n4dO1hTfucIEAmJSh2fsvcI8oRgzX-me?usp=drive_link"
link2 = "https://drive.google.com/drive/folders/1jTEG4w09NdcLkzl_A7uNGMOSSVFCx5N8"

# HTML for side-by-side buttons with bigger size, rounded edges, darker green
buttons_html = f"""
<div style="display:flex; gap:20px; margin-top:20px;">
    <a href="{link1}" target="_blank">
        <button style="
            background-color: #A3C389;  /* slightly darker green */
            color: black;
            border: 2px solid black;
            padding: 20px 40px;          /* bigger button */
            font-size: 20px;             /* bigger text */
            font-weight: bold;
            border-radius: 15px;         /* rounded edges */
            cursor: pointer;
        ">Iloilo City Datasets</button>
    </a>
    <a href="{link2}" target="_blank">
        <button style="
            background-color: #A3C389;
            color: black;
            border: 2px solid black;
            padding: 20px 40px;
            font-size: 20px;
            font-weight: bold;
            border-radius: 15px;
            cursor: pointer;
        ">Iloilo City Datasets (Standardized)</button>
    </a>
</div>
"""

st.markdown(buttons_html, unsafe_allow_html=True)
