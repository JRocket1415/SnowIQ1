import streamlit as st
from snowiq import st_custom_slider

v_custom = st_custom_slider('Hello world', 0, 100, '', key="slider1")
st.set_page_config(layout="wide")
st.write(v_custom)