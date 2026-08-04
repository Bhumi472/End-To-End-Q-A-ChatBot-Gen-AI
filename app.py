import streamlit as st

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant. Answer the user's questions clearly and accurately."
        ),
        (
            "user",
            "Question: {question}"
        )
    ]
)

# Function to generate response
def generate_response(question, model_name, temperature):

    llm = Ollama(
        model=model_name,
        temperature=temperature
    )

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    return chain.invoke({"question": question})


# Streamlit UI
st.set_page_config(
    page_title="Q&A Chatbot with Ollama",
    page_icon="🤖"
)

st.title("🤖 Q&A Chatbot with Ollama")

st.sidebar.header("Settings")

# Model Selection
model = st.sidebar.selectbox(
    "Select Model",
    ["mistral"]
)

# Temperature
temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

st.write("Ask me anything!")

user_input = st.text_input("Your Question")

if st.button("Generate Response"):

    if user_input.strip():

        with st.spinner("Generating response..."):

            response = generate_response(
                user_input,
                model,
                temperature
            )

        st.success("Response")
        st.write(response)

    else:
        st.warning("Please enter a question.")