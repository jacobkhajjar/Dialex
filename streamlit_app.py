import streamlit as st
from lexiguess import lexiguess

st.title("Lexical Set Guesser")

entry = st.text_input("entry", label_visibility="hidden")

if entry:
    result = lexiguess(entry)
    st.write("  \n  \n".join(result))
else:
    st.write("Type words above, separated by a space. Then press enter to see the lexical sets.")