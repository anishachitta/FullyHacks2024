import streamlit as st
import requests

def generate_response(prompt):
    # Set up the OpenAI API endpoint
    endpoint = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    # Set up your OpenAI API key
    api_key = "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"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 50
    }
    # Send a POST request to the OpenAI API
    response = requests.post(endpoint, json=data, headers=headers)
    
    # Print the entire response
    print(response.text)
    
    # Extract and return the generated response
    response_json = response.json()
    
    if 'choices' in response_json:
        return response_json['choices'][0]['text'].strip()
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