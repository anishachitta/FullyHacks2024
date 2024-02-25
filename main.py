import streamlit as st
import requests

def generate_response(prompt):
    # Set up the OpenAI API endpoint
    endpoint = "https://api.openai.com/v1/chat/completions"  # Update the endpoint here
    # Set up your OpenAI API key
    api_key = "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"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo-0125",  # Specify the model here
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    # Send a POST request to the OpenAI API
    response = requests.post(endpoint, json=data, headers=headers)
    
    # Print the entire response
    print(response.text)
    
    # Extract and return the generated response
    response_json = response.json()
    
    if 'choices' in response_json:
        return response_json['choices'][0]['message']['content'].strip()  # Correct key to extract response
    else:
        # Handle the case where the response format has changed
        return "Unexpected response format."


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