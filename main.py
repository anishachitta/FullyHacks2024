
import streamlit as st
import requests
import os

def generate_response(prompt):
    # Set up the OpenAI API endpoint
    endpoint = "https://api.openai.com/v1/engines/davinci/completions"
    # Set up your OpenAI API key
    api_key = os.gentenv("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")
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
    # Create a sidebar
    st.sidebar.title("Chat Settings")
    # Create a text input for the user message

    user_input = st.text_input("You: ")
    # Create a button to send the message

    if st.button("Send"):
        # Display the user message
        st.write(f"You: {user_input}")
        # Here you would typically generate and display the chatbot's response
        # But for this example, we'll just echo the user's message
        st.write(f"Chatbot: {user_input}")
        # Generate response using ChatGPT
        chatbot_response = generate_response(user_input)
        st.write(f"Chatbot: {chatbot_response}")

if __name__ == "__main__":
    main()
