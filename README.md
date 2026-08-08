# 🤖 End-to-End Q&A ChatBot Gen AI

### 🚀 End-to-End Question Answering ChatBot using LangChain, Streamlit, OpenAI, Groq & Ollama

Build intelligent Q&A chatbots using cloud-based **OpenAI and Groq models** or completely local open-source models powered by **Ollama**.

⭐ If you find this project helpful, don't forget to star the repository!

---

# 📖 Overview

This project demonstrates how to build modern AI-powered Question & Answer chatbots using **LangChain** and **Streamlit**.

The repository contains multiple implementations using different LLM providers:

* 🌐 **OpenAI-based chatbot** using GPT models
* ⚡ **Groq-based chatbot** using Llama models
* 💻 **Local chatbot** using Ollama and open-source LLMs such as Mistral

The applications provide a simple interface for asking questions and receiving AI-generated responses.

---

# ✨ Features

* 🤖 AI Question Answering
* 🌐 OpenAI GPT Integration
* ⚡ Groq LLM Integration
* 💻 Ollama Local LLM Support
* 📱 Streamlit Web Interface
* ⚡ LangChain Prompt Templates
* 🔄 Output Parsing
* 🎛 Adjustable Temperature
* 🔒 Local AI Execution with Ollama
* ☁ Cloud AI Execution with OpenAI & Groq
* 🔑 API Key Authentication for Cloud Models

---

# 📂 Repository Structure

```text
End-To-End-Q-A-ChatBot-Gen-AI/
│
├── README.md
├── requirements.txt
│
├── 2-OpenAI Chatbot
│   └── app.py
│
├── groq-chatbot.py
│
└── ollama chatbot.py
```

---

# 🚀 Chatbot Implementations

## 🌐 OpenAI Chatbot

Features

* GPT Model Support
* API Key Authentication
* Adjustable Temperature
* Interactive Streamlit UI
* LangChain Integration

Requirements

* OpenAI API Key
* Internet Connection

---

## ⚡ Groq Chatbot

Features

* Groq API Integration
* Llama Model Support
* Fast Cloud LLM Inference
* API Key Authentication
* Adjustable Temperature
* Interactive Streamlit UI
* LangChain Integration

Supported Models

* Llama 3.1 8B Instant
* Llama 3.3 70B Versatile

Requirements

* Groq API Key
* Internet Connection

---

## 💻 Ollama Chatbot

Features

* Local AI Inference
* No API Key Required
* Privacy Friendly
* Open Source Models
* Local LLM Execution
* Interactive Streamlit UI

Supported Models

* Mistral
* Llama
* Gemma
* Phi

Requirements

* Ollama Installed
* Downloaded LLM Model

---

# 🛠 Tech Stack

| Category           | Technology         |
| ------------------ | ------------------ |
| Language           | Python             |
| Framework          | LangChain          |
| UI                 | Streamlit          |
| Cloud Model        | OpenAI GPT         |
| Cloud Model        | Groq Llama         |
| Local Model        | Ollama             |
| Prompt Engineering | ChatPromptTemplate |
| Output Parsing     | StrOutputParser    |

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Bhumi472/End-To-End-Q-A-ChatBot-Gen-AI.git
```

Navigate to the project:

```bash
cd End-To-End-Q-A-ChatBot-Gen-AI
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Or install the required packages manually:

```bash
pip install streamlit langchain langchain-core langchain-groq
```

For OpenAI support:

```bash
pip install langchain-openai
```

For Ollama support:

```bash
pip install langchain-community
```

---

# 🔑 OpenAI Setup

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
LANGCHAIN_API_KEY=your_langsmith_key
```

Make sure you never upload your API keys to GitHub.

---

# ⚡ Groq Setup

Create a Groq API key and configure it as an environment variable:

```env
GROQ_API_KEY=your_groq_api_key
```

For Streamlit Cloud, add the API key through **Secrets / Advanced Settings**:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

The Groq chatbot uses the LangChain `ChatGroq` integration.

---

# 💻 Ollama Setup

Install Ollama:

https://ollama.com

Download Mistral:

```bash
ollama pull mistral
```

Start Ollama:

```bash
ollama serve
```

Verify installation:

```bash
ollama list
```

---

# ▶ Running the OpenAI Chatbot

Navigate to the OpenAI chatbot directory:

```bash
cd "2-OpenAI Chatbot"
```

Run:

```bash
streamlit run app.py
```

---

# ▶ Running the Groq Chatbot

From the project root:

```bash
streamlit run groq-chatbot.py
```

---

# ▶ Running the Ollama Chatbot

From the project root:

```bash
streamlit run "ollama chatbot.py"
```

---

# 📸 Application Workflow

```text
User Question
      │
      ▼
Streamlit Interface
      │
      ▼
LangChain Prompt
      │
      ▼
┌────────────────────────────┐
│       Select LLM Provider  │
├────────────────────────────┤
│ OpenAI                     │
│ Groq                       │
│ Ollama                     │
└──────────────┬─────────────┘
               │
               ▼
      Generated Response
               │
               ▼
       Display in Streamlit
```

---

# 🔄 LangChain Workflow

The chatbot follows a simple LangChain pipeline:

```text
ChatPromptTemplate
        │
        ▼
       LLM
        │
        ▼
 StrOutputParser
        │
        ▼
    Final Answer
```

The core chain follows:

```python
chain = prompt | llm | output_parser
```

---

# 📊 Cloud vs Local AI

| Feature              | OpenAI         | Groq           | Ollama        |
| -------------------- | -------------- | -------------- | ------------- |
| Execution            | Cloud          | Cloud          | Local         |
| API Key              | Required       | Required       | Not Required  |
| Internet             | Required       | Required       | Not Required* |
| Local Inference      | ❌              | ❌              | ✅             |
| Open Source Models   | ❌              | ✅              | ✅             |
| Privacy              | Standard Cloud | Standard Cloud | High          |
| Hardware Requirement | Low            | Low            | Higher        |

* Internet is required to initially download Ollama models.

---

# 📚 Learning Outcomes

By completing this project, you'll learn:

* LangChain Basics
* Prompt Templates
* Streamlit Development
* OpenAI Integration
* Groq Integration
* Ollama Integration
* Cloud LLM Integration
* Local LLM Deployment
* Output Parsing
* Temperature Control
* AI Application Development

---

# 🔮 Future Improvements

* Conversation Memory
* Chat History
* PDF Question Answering
* RAG Pipeline
* Vector Database Integration
* Multiple LLM Providers
* Multiple Local Models
* Voice Chat
* Image Input Support
* Docker Deployment
* Authentication
* LLM Observability
* Prompt Evaluation

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ Show Your Support

If you enjoyed this project, please consider giving it a ⭐ on GitHub.

Happy Coding! 🚀
