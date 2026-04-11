# DataTalk

Ask questions on your CSV and PDF files using AI. Upload a file, type your question, get an answer.

## Tech Stack
- Streamlit
- Pandas
- PyMuPDF
- Groq API (llama-3.3-70b-versatile)

## Setup

1. Clone the repo
2. Install dependencies
uv sync
3. Create a `.env` file in the root:
GROQ_API_KEY=your_key_here
4. Run the app
streamlit run app.py

## Usage
- Upload a CSV or PDF file
- Type your question
- Click Send