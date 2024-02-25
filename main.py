import streamlit as st
import requests

def generate_response(prompt):
    # Set up the OpenAI API endpoint
    endpoint = "https://api.openai.com/v1/engines/davinci/completions"
    # Set up your OpenAI API key
    api_key = "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"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "davinci",
        "prompt": prompt,
        "max_tokens": 50
    }
    # Send a POST request to the OpenAI API
    response = requests.post(endpoint, json=data, headers=headers)
    # Extract and return the generated response
    return response.json()["choices"][0]["text"].strip()

def main():
    st.title("Neon Chatbot UI")
    st.sidebar.title("Chat Settings")
    
    user_input = st.text_input("You: ")
    
    if st.button("Send"):
        st.write(f"You: {user_input}")
        # Generate response using ChatGPT
        chatbot_response = generate_response(user_input)
        st.write(f"Chatbot: {chatbot_response}")

if __name__ == "__main__":
    main()
