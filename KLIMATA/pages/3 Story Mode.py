import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import json
import streamlit.components.v1 as components
import os # Imported os for path handling

# --- FIX 1: This must be the FIRST Streamlit command ---
st.set_page_config(layout="wide", page_title="ArcGIS Story Mode")

st.title("ArcGIS Story Mode")
st.markdown("*Your Ultimate Guided Experience with KLIMATA!*")

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

hide_streamlit_style = """
    <style>
    /* Hide header and hamburger menu */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- FIX 2: Robust Path Handling ---
# This assumes the image is in the ROOT directory (parent of 'pages')
# If the image is inside the 'pages' folder, remove the '..'
try:
    # Construct absolute path to avoid "File not found" errors
    # Adjust ".." if the image is in the same folder vs root folder
    # If 'klimata_logo.png' is in the root folder and this script is in /pages:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir) # Go up one level to root
    logo_path = os.path.join(parent_dir, "klimata_logo.png")
    
    st.sidebar.image(logo_path, use_column_width=True) # Use column width is safer than fixed 1000px for sidebars
except Exception as e:
    st.sidebar.error(f"Logo not found. Checked path: {logo_path}")


components.html(
    """
    <div style="
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    ">
        <iframe 
            src="https://storymaps.arcgis.com/stories/47240a5087554d809c247692e43b3ab0"
            width="100%" 
            height="900px"
            style="border:none; border-radius: 10px;"
            allowfullscreen 
            allow="geolocation">
        </iframe>
    </div>
    """,
    height=950, 
)

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
