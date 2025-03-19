import streamlit as st 
import numpy as np
from helper import item_info as info

item_list = ["Blazer","Button shirts","Denim jacket","Hoodie","Jeans","Long pants","Shorts","T shirt"]
# Initialize session state of sections if it doesn't exist
if 'section' not in st.session_state:
    st.session_state.section = 0

with st.sidebar:
    with st.container(border=True):
        for index, item in enumerate(item_list):
            if st.button(f'section: {item} {index}',key=index, use_container_width = True, type="secondary"):
                st.session_state.section = index
        st.html("""<style>[data-testid="stBaseButton-secondary"] {text-align: left;justify-content: flex-start;}</style>""")

st.write(st.session_state.section)
info.item(st.session_state.section)

