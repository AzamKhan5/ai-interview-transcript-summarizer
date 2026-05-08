# Interview Transcript Summarizer

A simple Streamlit application that summarizes interview transcripts using the Gemini API.

The app generates:

1. Topics Covered  
2. Candidate Profile  
3. Candidate Summary  

---

# Tech Stack

- Python
- Streamlit
- Google Gemini API

---

# LLM Provider and Model

- Provider: Google Gemini
- Model Used: `gemini-2.5-flash`

```python
model = genai.GenerativeModel("gemini-2.5-flash")
```

---

# Project Structure

```text
project-folder/
│
├── summarizer.py
├── requirements.txt
├── .gitignore
├── README.md
└── prompt_iterations.md
```

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone <your-repo-link>
cd <repo-name>
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Dependencies

```txt
streamlit
google-generativeai
python-dotenv
```

---

# Add Gemini API Key

Create a `.env` file in the project root folder.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

Do NOT upload the `.env` file to GitHub.

---

# Run the Application

```bash
streamlit run summarizer.py
```

After running the command, Streamlit will open the app in your browser.

---

# How It Works

1. Upload a `.txt` interview transcript
2. Click **Generate Summary**
3. Gemini analyzes the transcript
4. The app generates:
   - Topics Covered
   - Candidate Profile
   - Candidate Summary

---

# Reflection

One thing that surprised me was how well Gemini handled long interview transcripts with a relatively simple prompt. Even without complex prompt engineering or multi-step workflows, the model was able to identify candidate strengths, role fit, and discussion topics quite accurately for both technical and management-style interviews.

If I had another day, I would improve the formatting and add export options such as downloading summaries as PDF or Markdown. I would also add support for `.docx` transcript uploads and better error handling for empty or unclear transcripts.

One limitation of the final prompt is that the role/seniority prediction may sometimes be too generic or slightly inaccurate, especially when the transcript does not contain enough technical depth or background information. The summaries also depend heavily on how clearly the candidate communicates during the interview.
