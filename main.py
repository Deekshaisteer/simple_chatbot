import os
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
# from constants import openai_key

# Set the API key
os.environ["GOOGLE_API_KEY"] ="your api key"


# Initialize the Streamlit app
st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Enter your input")

# Initialize conversation history if not already done
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = []

# Function to update conversation history
def update_conversation_history(user_input, response):
    st.session_state['conversation_history'].append(f"User: {user_input}")
    st.session_state['conversation_history'].append(f"Bot: {response}")

# Initialize the LLM with the correct model
llm = GoogleGenerativeAI(model="gemini-pro", temperature=0.8)

# Check if there's an input from the user
if input_text:
    # Include conversation history in the input
    conversation_input = "\n".join(st.session_state['conversation_history']) + f"\nUser: {input_text}\nBot:"
    
    # Generate the response from the LLM
    response = llm(conversation_input)
    
    # Update the conversation history
    update_conversation_history(input_text, response)
    
    # Display the response
    st.write(response)
