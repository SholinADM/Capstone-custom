import streamlit as st 
from PIL import Image
import numpy as np
import json
import cv2
import base64
import os
from helper.GenbotAPI import extract_message, run_flow
from helper import item_info as info

#load the model for image prediction
@st.cache_resource
def load_model(filepath):
    import keras  
    model = keras.saving.load_model(filepath, custom_objects=None, compile=True, safe_mode=True)
    return model
    
#predict the type of clothe in the image
def predict_image(image,class_names):
    image = Image.open(image)
    image = np.array(image)
    image = cv2.resize(image, (160,160))
    image = np.expand_dims(image, axis=0)
    predict = np.argmax(model.predict(image))
    st.session_state.section = predict
    predicted_class = class_names[predict]
    return predicted_class
#Save chat messages from chatbot in text file
def save_conversation():
    with open("conversation.txt", "w", encoding="utf-8") as file:
        for message in st.session_state.messages:
            role = "User" if message["role"] == "user" else "Bot"
            file.write(f"{role}: {message['content']}\n")
    st.success("Conversation saved as conversation.txt 📁")
#clear chat messages from chatbox
def clear_chat():
    st.session_state.messages = []
    st.session_state.chatbot = False
    st.session_state.initiate_uploader = False
    st.session_state.image = None
    #initialize chat so the bot greets user instead of user greeting the bot
    st.rerun()
# Function to creates download popups
def download_json(data):
    json_data = json.dumps(data)
    json_bytes = json_data.encode('utf-8')
    return json_bytes
# Background CSS Function
def set_bg_image(image_url):
    bg_css = f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

def get_image_as_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

#Declare constants
model = load_model(os.path.join('models','model_class.keras'))
class_names = ['Blazer', 'Denim_Jacket', 'Hoodie', 'Jeans', 'Shorts', 'T shirt', 'button_shirts', 'long_pants']
TWEAKS = {
  "TextInput-HqNiz": {},
  "TextInput-NZgrh": {}
}
# Initialize session state for chat history 
if "messages" not in st.session_state: 
    st.session_state.messages= []
    #initialize chat so the bot greets user instead of user greeting the bot
    assistant_response = extract_message(run_flow("hello",TWEAKS))
    st.session_state.messages.append({
                "role": "assistant", 
                "content": assistant_response,
                "avatar": "🤖"
            })
# Initialize session state for the image if it doesn't exist
if 'image' not in st.session_state:
    st.session_state.image = None
# Initialize session state for chatbot
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = False
# Initialize session state for image uploader
if 'initiate_uploader' not in st.session_state:
    st.session_state.initiate_uploader = False
# Initialize session state of sections if it doesn't exist
if 'section' not in st.session_state:
    st.session_state.section = None


# Streamlit App 
def main():
    image_base64 = get_image_as_base64(os.path.join(os.getcwd(),"static","background.jpg"))
    
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background: url("data:image/png;base64,{image_base64}") no-repeat center center fixed;
            background-size: 100% 100%; /* Ensures the whole image fits */
            background-repeat: no-repeat; /* Prevents tiling */
        }}
        [data-testid="stVerticalBlock"] {{
        background: rgba(0, 0, 0, 0.5) !important; /* Semi-transparent containers */
        border-radius: 10px;
        padding: 10px;
        }}
        [data-testid="stChatInputContainer"] {{
        display: none !important;
        }}
        """,
        unsafe_allow_html=True
        )

    st.title("Fashionista 🤖")
    st.subheader("Hey there! 👗✨ I’m Fashionista Bot, your personal AI stylist!")
    st.write("Struggling with outfit choices? I’ve got you covered! Whether it’s a casual day out, a business meeting, or a special occasion, I help you decide what to wear based on the weather, event, and your personal style.I analyze fashion trends, consider your wardrobe preferences, and even check the forecast to make sure you’re stylish and comfortable. Need shopping suggestions? I can recommend pieces to complete your look! Let’s find the perfect outfit together! What’s the occasion today? 💃🕺" )
    with st.sidebar:
        st.subheader("Item list:")
        with st.container(border=True):
            for index, item in enumerate(class_names):
                if st.button(f'{item}',key=index, use_container_width = True, type="secondary"):
                    st.session_state.section = index
            st.html("""<style>[data-testid="stBaseButton-secondary"] {text-align: left;justify-content: flex-start;}</style>""")

    if st.session_state.section is None:
        pass
    elif st.session_state.section > 7:
            st.warning("There're only 8 items")
    elif st.session_state.section is not None:
        info.item(st.session_state.section)

    if not st.session_state.chatbot:
        st.subheader("Need a help?")
        if st.button("Ask our Fashionista 🤖"):
            st.session_state.chatbot = True
            st.rerun()

    if st.session_state.chatbot:
        #File uploader for image
        if not st.session_state.initiate_uploader:
            if st.button("Upload image"):
                st.session_state.initiate_uploader = True
        if st.session_state.initiate_uploader:
            enable = st.checkbox("Enable camera")
            if enable:
                st.session_state.image = st.camera_input("Take a picture")
            else:
                st.session_state.image = st.file_uploader("Upload an image (JPG, PNG)", type=["jpg", "jpeg", "png"])
            if st.session_state.image is not None:
                #predict the image class when uploaded
                clothes_type = predict_image(st.session_state.image,class_names)
                #Insert the image classification result to tweak to be sent together with query
                TWEAKS["TextInput-HqNiz"]["input_value"] = clothes_type
                st.toast("image uploaded")
                st.image(st.session_state.image,width=160)
                st.write(f"image detected: {clothes_type}")
            
        # display previous messages with avatars 
        for messages in st.session_state.messages: 
            with st.chat_message(messages["role"], avatar=messages["avatar"]):
                st.write(messages["content"])
                
        # input box for user message 
        if query := st.chat_input("Enter your queries."):
            # Add user message to session state 
            st.session_state.messages.append({
                    "role": "user",
                    "content": query,
                    "avatar": "😸"
                })
            with st.chat_message("user", avatar="😸"): 
                st.write(query) # here is to display user message 
                
            # call Langdlow API and get the assistant's response after user ask question 
            with st.chat_message("assistant", avatar="🤖"):
                message_placeholder = st.empty() # this is a placeholder for assistant response 
                with st.spinner("Thinking......"): 
                    #Format and send chat log to langflow
                    formatted_log = "\n".join([f"[{index}] {entry['role']}: {entry['content']} \n" 
                                               for index,entry in enumerate(st.session_state.messages)])
                    TWEAKS["TextInput-NZgrh"]["input_value"] = formatted_log
                    # Fetch response from Langflow 
                    assistant_response = extract_message(run_flow(query,TWEAKS))
                    message_placeholder.write(assistant_response)
                
            # Add assistant response to the session state 
            st.session_state.messages.append({
                    "role": "assistant", 
                    "content": assistant_response,
                    "avatar": "🤖"
                })
        #Put buttons to downloan and clear chat
        left, right = st.columns(2)
        with left:
            st.download_button(label="💾 Download Conversation",
                            data=download_json(st.session_state.messages),
                            file_name="session_state_message.txt",
                            mime="text/plain")
        with right:
            if st.button("🗑️ Clear Chat History"):
                clear_chat()

if __name__ == "__main__": 
    main()