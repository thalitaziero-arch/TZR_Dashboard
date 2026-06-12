import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="TZR Dashboard", layout="wide")

with open("tzr_v3_white.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=3000, scrolling=True)