import streamlit as st

pg = st.navigation([
    st.Page("pages/home.py", title="Lexiguess", icon="🕵️", default=True),
    st.Page("pages/about.py", title="How it Works")
], position="top")

pg.run()