import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import json
import os

# Set page config to wide layout - MUST BE FIRST
st.set_page_config(layout="wide", page_title="Amenity Dashboard")

st.title("Amenity Dashboard")
st.markdown("*An Essential Guide of Barangay Amenities!*")

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

# --- FIX: Robust Path Handling for Logo ---
try:
    # Get the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the root directory
    parent_dir = os.path.dirname(current_dir)
    # Construct the full path to the image
    logo_path = os.path.join(parent_dir, "klimata_logo.png")
    
    # Use use_column_width for better sidebar scaling
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

st.components.v1.html(
    """
    <div style="
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        width: 100%;
        height: 1000px;  /* slightly taller than iframe to include padding */
        box-sizing: border-box;
    ">
        <iframe src="https://xcc15.github.io/Team-Bernoulli/"
                style="width:100%; height:100%; border:none;">
        </iframe>
    </div>
    """,
    height=1000,
)
