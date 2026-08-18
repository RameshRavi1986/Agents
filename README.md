# CSV Q&A App

A Streamlit web app that allows you to upload CSV files and ask questions about your data in plain English, powered by LangChain and Claude AI (Anthropic).

---

## Requirements

- Python 3
- pip3

---

## Setup

### 1. Clone the repository

```bash
git clone [Streamlit-langchain](https://github.com/RameshRavi1986/Agents.git)
cd Streamlit-langchain
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate virtual environment

```bash
# Mac/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 5. Create your `.env` file

Create a file called `.env` in the project root and add your Anthropic API key:

```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

> **Get your API key at:** [console.anthropic.com](https://console.anthropic.com)

### 6. Run the app

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## Usage

1. Upload one or more CSV files using the file uploader
2. Type your question in the text box
3. Click **Ask Agent**
4. Get your answer powered by Claude AI

---

## Tech Stack

| Tool | Purpose |
|---|---|
| [Streamlit](https://streamlit.io) | Web app framework |
| [LangChain](https://langchain.com) | AI agent framework |
| [Claude (Anthropic)](https://anthropic.com) | AI language model |
| [Pandas](https://pandas.pydata.org) | Data processing |
| [python-dotenv](https://pypi.org/project/python-dotenv) | Environment variables |

---

## Project Structure

```
https://github.com/RameshRavi1986/
agents/                        
├── streamlit-langchain/      
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
├── .gitignore                
└── README.md                  
```

---

## Dependencies

`requirements.txt`:

```
streamlit
pandas
python-dotenv
langchain
langchain-anthropic
langchain-experimental
anthropic
```

---

## .gitignore

Make sure your `.gitignore` includes:

```
.env
.venv/
__pycache__/
*.pyc
```

> **Important:** Never commit your `.env` file — it contains your private API key.
