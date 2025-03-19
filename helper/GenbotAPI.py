from typing import Optional
import requests 
import streamlit as st

# Constants 
BASE_API_URL = "http://127.0.0.1:7860"
FLOW_ID = "1a5fcab9-db79-41b1-8104-e1149c1d7e13"
ENDPOINT = "" # You can set a specific endpoint name in the flow settings

# Function to run the flow 
def run_flow(message: str,tweaks: Optional[dict] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param endpoint: The ID or the endpoint name of the flow
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/api/v1/run/{ENDPOINT or FLOW_ID}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    if tweaks:
        payload["tweaks"] = tweaks

    response = requests.post(api_url, json=payload)
    return response.json()

#save the conversation with AI bot in text file
def save_conversation():
    with open("conversation.txt", "w", encoding="utf-8") as file:
        for message in st.session_state.messages:
            role = "User" if message["role"] == "user" else "Bot"
            file.write(f"{role}: {message['content']}\n")
    st.success("Conversation saved as conversation.txt 📁")
#clear the local memmory of the chat
def clear_chat():
    st.session_state.messages = [] 
    st.rerun()

# Function to extract the desired message 
def extract_message(response: dict) -> str: 
    try: 
        # Navigate to the message inside the response structure 
        return response['outputs'][0]['outputs'][0]['results']['message']['text']
    except(KeyError, IndexError):
        return "No valid message found in response."

 