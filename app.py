import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="AIDEOM-VN Dashboard")

with open("index.html", "r", encoding="utf-8") as f:
    html_string = f.read()

components.html(html_string, height=1200, scrolling=True)
