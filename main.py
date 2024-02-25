import streamlit as st

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

if __name__ == "__main__":
    main()
