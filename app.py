import os
from gtts import gTTS

# ---- Agent: Search ----
def search_papers(topics):
    return [
        {"title": "AI in Medicine", "text": "AI is transforming healthcare.", "topic": "Artificial Intelligence"},
        {"title": "Climate Models", "text": "Climate models predict global warming.", "topic": "Climate Change"},
        {"title": "AI Ethics", "text": "Ethical concerns are rising in AI.", "topic": "Artificial Intelligence"},
    ]

# ---- Agent: Processing ----
def process_pdf(paper):
    paper["clean_text"] = paper["text"].strip()
    return paper

# ---- Agent: Classification ----
def classify_topic(papers, topics):
    return [p for p in papers if p["topic"] in topics]

# ---- Agent: Summarization ----
def summarize(paper):
    return {
        "title": paper["title"],
        "summary": f"{paper['title']} - Summary: {paper['clean_text']}",
        "topic": paper["topic"]
    }

# ---- Agent: Synthesis ----
def synthesize(summaries):
    result = {}
    for s in summaries:
        topic = s["topic"]
        if topic not in result:
            result[topic] = []
        result[topic].append(s["summary"])
    combined = {k: "\n".join(v) for k, v in result.items()}
    return combined

# ---- Agent: Audio ----
def generate_audio(synthesis):
    os.makedirs("audio_outputs", exist_ok=True)
    for topic, text in synthesis.items():
        tts = gTTS(text)
        filename = f"audio_outputs/{topic.replace(' ', '_')}.mp3"
        tts.save(filename)
        print(f"[✓] Audio generated: {filename}")

# ---- Main Orchestration ----
def main():
    topics = ["Artificial Intelligence", "Climate Change"]
    print("[*] Searching papers...")
    papers = search_papers(topics)

    print("[*] Processing papers...")
    processed = [process_pdf(p) for p in papers]

    print("[*] Classifying topics...")
    classified = classify_topic(processed, topics)

    print("[*] Summarizing papers...")
    summaries = [summarize(p) for p in classified]

    print("[*] Synthesizing by topic...")
    synthesis = synthesize(summaries)

    print("[*] Generating audio...")
    generate_audio(synthesis)

    print("[✓] Pipeline complete. Summaries and audio files are ready!")

if __name__ == "__main__":
    main()
