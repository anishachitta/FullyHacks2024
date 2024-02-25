import streamlit as st
import requests
from openai import OpenAI

def generate_response(prompt):
    # Set up the OpenAI API endpoint for chat completions
    chat_endpoint = "https://api.openai.com/v1/chat/completions"
    
    # Set up the OpenAI API endpoint for image generation
    image_endpoint = "https://api.openai.com/v1/images/generate"
    
    # Set up your OpenAI API key
    api_key = "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"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
   # ChatGPT Request
    chat_response = requests.post(chat_endpoint, json=chat_data, headers=headers)
    chat_response_json = chat_response.json()

    # Check if 'choices' is in the response
    if 'choices' in chat_response_json:
        chatbot_response = chat_response_json['choices'][0]['message']['content'].strip()
    else:
        chatbot_response = "Unexpected response format from ChatGPT."

    # ... (same as before)

    return chatbot_response, image_url

def main():
    st.title("Neon Chatbot UI")
    st.sidebar.title("Chat Settings")
    
    user_input = st.text_input("You: ")
    
    if st.button("Send"):
        st.write(f"You: {user_input}")
        # Generate response using ChatGPT and DALL·E
        chatbot_response, image_url = generate_response(user_input)
        st.write(f"Chatbot: {chatbot_response}")
        st.image(image_url, caption='DALL·E Generated Image', use_column_width=True)

if __name__ == "__main__":
    main()
