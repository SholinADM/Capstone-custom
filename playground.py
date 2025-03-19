import streamlit as st

# Hide chat input bar with CSS
hide_chat_input = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #FFFFFF !important; /* Light mode */
    color: white !important; /* Ensures text is visible */
}
[data-testid="stChatInputContainer"] {
    display: none !important;
    height: 0px !important;
    visibility: hidden !important;
}
/* Hide any extra spacing at the bottom */
main { padding-bottom: 0px !important; }
</style>
</style>
"""

st.markdown(hide_chat_input, unsafe_allow_html=True)

st.title("Fashionista Bot 🛍️")
st.write("Helping you decide what to wear!")

# Chat input remains functional
user_message = st.chat_input("Ask me about outfits...")

if user_message:
    with st.chat_message("user"):
        st.write(user_message)

    with st.chat_message("assistant"):
        st.write("Great choice! Let me suggest an outfit...")
