# Python Voice Assistant

A beginner-friendly Python voice assistant that listens to spoken commands and responds using speech.
The assistant can greet the user, tell the current time and date, perform web searches, and handle unclear voice input gracefully.

---

## Features

### Beginner Tier

- Capture voice input using `speech_recognition`
- Respond to greetings such as “Hello”
- Tell the current time
- Tell the current date
- Perform a web search on a spoken topic
- Graceful error handling if speech is not understood
- Text-to-speech feedback using `pyttsx3`

### Planned Advanced Features

- Weather API integration
- NLP-based intent recognition using `nltk` or `transformers`
- Email sending using `smtplib`
- Open websites/apps using voice commands
- Reminders and task management
- Wake word support

---

## Tech Stack

- Python
- SpeechRecognition
- pyttsx3
- datetime
- webbrowser

Advanced version:

- nltk / transformers
- smtplib
- third-party APIs

---

## Project Structure

```bash
voice-assistant/
│── app/
│   │── __init__.py
│   │── assistant.py
│   │── speech_engine.py
│   │── commands.py
│   │── utils.py
│
│── docs/
│   │── project-notes.md
│
│── tests/
│   │── test_commands.py
│
│── .gitignore
│── README.md
│── requirements.txt
│── run.py
```
