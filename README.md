# Research-Paper-Summarization-Multi-Agent-System

Research Agent is a multi-agent AI system that searches for academic papers, summarizes them, organizes by topic, and generates audio podcast summaries.
It’s designed to help researchers, students, and professionals stay up-to-date with research across multiple domains—quickly and efficiently.

📁 Folder Structure
├── app.py
├── requirements.txt
├── sample_input_output/
│   ├── sample_input.txt
│   └── sample_output.txt
├── audio_outputs/
├── README.md


⚙️ Setup Instructions
Clone the repo
git clone https://github.com/Karthikbulusu18/research-agent.git
cd research-agent


Install dependencies
pip install -r requirements.txt

Run the application
python app.py

Or use Docker:
docker build -t research-agent .
docker run -p 8501:8501 research-agent


✨ Features
Topic-based research paper search (mocked in prototype)
Document preprocessing and topic classification
AI-generated summaries for each paper
Cross-paper synthesis grouped by topic
Text-to-speech audio generation (MP3 podcast style)
Easily extendable for real-world APIs like arXiv, Crossref, etc.

🧪 Sample Input/Output
Check the sample_input_output/ folder to view:
sample_input.txt: Example list of topics
sample_output.txt: Summarized and synthesized results
Generated audio files are stored in audio_outputs/.

🧰 Tech Stack
Python

gTTS (Google Text-to-Speech)

Modular multi-agent design

CLI-based orchestration (Streamlit version optional)

