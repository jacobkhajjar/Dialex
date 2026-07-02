import streamlit as st

st.header("How Lexiguess Works", divider="rainbow")

st.markdown(
    '''
    Lexiguess works by first looking up the word in the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) which will give the General American pronunciation of the word.
    It then follows some steps until it has determined the best guess at what lexical set each vowel phoneme belongs to.
    1. If the lexical set is clear from the American pronunciation alone (e.g. KIT, DRESS, etc.) then it stops here.
    2. It looks up the word in a second dictionary, [Britphone](https://github.com/JoseLlarena/Britfone) which will find the RP pronunciation of the word. If comparing the GenAm and RP pronunciation is enough (e.g. if it is /a/ in GenAm but /ɑ/ in RP, it's BATH) then it stops here.
    3. If pronunciation alone doesn't have the answer, it then checks a set of spelling rules as defined by Eric Armstrong in his book [Lexical Sets for Actors](https://ecampusontario.pressbooks.pub/lexicalsets/).
    4. If the lexical set can't be determined by these steps, then the possible sets will be presented as "ambiguous". This is common with differentiating NORTH from FORCE.

    If the word appears multiple times in the CMU dictionary, either for multiple pronunciations or homonoyms, each pronunciation will be displayed on a seperate line.

    e.g.:  
    read: DRESS  
    read: FLEECE
    '''
)