import streamlit as st
from lexiguess import lexiguess

st.header("Lexiguess", divider="rainbow")
st.write('''
    This tool will do its best to determine the lexical sets for any word.  
    Type words in the box below, separated by a space. Then press enter to see the lexical sets.
    ''')

entry = st.text_input("entry", label_visibility="hidden")

if entry:
    result = lexiguess(entry)
    st.write("  \n  \n".join(result))
else:
    st.write(":grey[awaiting input]")

st.divider()

st.write("This tool is developed by dialect coach Jacob Hajjar. If you have any feedback or encounter any errors, get in touch on instagram [@jacobkhajjar](www.instragram.com/jacobkhajjar)")

st.markdown('''Sources:  
- [The CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict)
- [Britfone](https://github.com/JoseLlarena/Britfone)
- [Lexical Sets for Actors](https://ecampusontario.pressbooks.pub/lexicalsets/) by Eric Armstrong''')

st.write(":grey[v1.0]")

