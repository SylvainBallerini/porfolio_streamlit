import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

import covid
import transport

PAGES = {
    "Covid" : covid,
    "Transport en Europe" : transport
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Allez à", list(PAGES.keys()))
page = PAGES[selection]
page.app()