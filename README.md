# 🤖 End-to-End Q&A ChatBot Gen AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-black?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-orange?style=for-the-badge)

### 🚀 End-to-End Question Answering ChatBot using LangChain, Streamlit, OpenAI & Ollama

Build intelligent Q&A chatbots using cloud-based OpenAI models or completely local open-source models powered by Ollama.

⭐ If you find this project helpful, don't forget to star the repository!

</div>

---

# 📖 Overview

This project demonstrates how to build modern AI-powered Question & Answer chatbots using **LangChain** and **Streamlit**.

The repository contains two implementations:

- 🌐 OpenAI-based chatbot using GPT models
- 💻 Local chatbot using Ollama and open-source LLMs (Mistral)

The applications provide a simple interface for asking questions and receiving AI-generated responses.

---

# ✨ Features

- 🤖 AI Question Answering
- 🌐 OpenAI GPT Integration
- 💻 Ollama Local LLM Support
- 📱 Streamlit Web Interface
- ⚡ LangChain Prompt Templates
- 🔄 Output Parsing
- 🎛 Adjustable Temperature
- 🔒 Local AI Execution (Ollama)
- ☁ Cloud AI Execution (OpenAI)

---

# 📂 Repository Structure

```text
End-To-End-Q-A-ChatBot-Gen-AI/
│
├── 2-OpenAI Chatbot/
│   ├── app.py
│   └── requirements.txt
│
├── 3-Ollama Chatbot/
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

---

# 🚀 Chatbot Implementations

## 🌐 OpenAI Chatbot

Features

- GPT-4o Support
- GPT-4 Turbo Support
- API Key Authentication
- Adjustable Temperature
- Interactive Streamlit UI

Requirements

- OpenAI API Key
- Internet Connection

---

## 💻 Ollama Chatbot

Features

- Local AI Inference
- No API Key Required
- Privacy Friendly
- Open Source Models
- Fast Local Responses

Supported Models

- Mistral
- Llama 3 (optional)
- Gemma (optional)
- Phi-3 (optional)

Requirements

- Ollama Installed
- Downloaded LLM Model

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Framework | LangChain |
| UI | Streamlit |
| Cloud Model | OpenAI GPT |
| Local Model | Ollama |
| Prompt Engineering | ChatPromptTemplate |
| Output Parsing | StrOutputParser |

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Bhumi472/End-To-End-Q-A-ChatBot-Gen-AI.git
```

Navigate to the project

```bash
cd End-To-End-Q-A-ChatBot-Gen-AI
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install streamlit langchain langchain-community langchain-openai python-dotenv
```

---

# 🔑 OpenAI Setup

Create a `.env` file

```env
OPENAI_API_KEY=your_api_key
LANGCHAIN_API_KEY=your_langsmith_key
```

---

# 💻 Ollama Setup

Install Ollama

https://ollama.com

Download Mistral

```bash
ollama pull mistral
```

Start Ollama

```bash
ollama serve
```

Verify installation

```bash
ollama list
```

---

# ▶ Running the OpenAI Chatbot

```bash
cd "2-OpenAI Chatbot"
streamlit run app.py
```

---

# ▶ Running the Ollama Chatbot

```bash
cd "3-Ollama Chatbot"
streamlit run app.py
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
OpenAI GPT / Ollama
      │
      ▼
Generated Response
      │
      ▼
Display in Streamlit
```

---

# 📚 Learning Outcomes

By completing this project, you'll learn:

- LangChain Basics
- Prompt Templates
- Streamlit Development
- OpenAI Integration
- Ollama Integration
- Local LLM Deployment
- AI Application Development

---

# 🔮 Future Improvements

- Conversation Memory
- Chat History
- PDF Question Answering
- RAG Pipeline
- Vector Database Integration
- Multiple Local Models
- Voice Chat
- Image Input Support
- Docker Deployment
- Authentication

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

<div align="center">

## ⭐ Show Your Support

If you enjoyed this project, please consider giving it a ⭐ on GitHub.

Happy Coding! 🚀

</div>
