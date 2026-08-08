import os
import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# -----------------------------
# Prompt Template
# -----------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant. "
            "Answer the user's questions clearly and accurately."
        ),
        (
            "user",
            "Question: {question}"
        )
    ]
)


# -----------------------------
# Function to Generate Response
# -----------------------------

def generate_response(question, model_name, temperature):

    llm = ChatGroq(
        model=model_name,
        temperature=temperature,
        api_key=os.getenv("GROQ_API_KEY")
    )

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    return chain.invoke({"question": question})


# -----------------------------
# Streamlit UI
# -----------------------------

st.set_page_config(
    page_title="Q&A Chatbot with Groq",
    page_icon="🤖"
)

st.title("🤖 Q&A Chatbot with Groq")

st.sidebar.header("Settings")


# -----------------------------
# Model Selection
# -----------------------------

model = st.sidebar.selectbox(
    "Select Model",
    [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile"
    ]
)


# -----------------------------
# Temperature
# -----------------------------

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)


# -----------------------------
# User Input
# -----------------------------

st.write("Ask me anything!")

user_input = st.text_input("Your Question")


# -----------------------------
# Generate Response
# -----------------------------

if st.button("Generate Response"):

    if user_input.strip():

        with st.spinner("Generating response..."):

            try:
                response = generate_response(
                    user_input,
                    model,
                    temperature
                )

                st.success("Response")
                st.write(response)

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter a question.")
