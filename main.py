import streamlit as st
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
