# 🎙️ Python Voice Assistant

A Python-based voice assistant that listens to spoken commands and performs useful tasks such as answering greetings, telling the current date and time, searching the web, sending emails, fetching live weather updates, setting reminders, and answering general knowledge questions. The project is designed to demonstrate speech recognition, text-to-speech, Natural Language Processing (NLP), API integration, and clean software architecture.

---

## 📌 Features

### Beginner Features

* 🎤 Capture voice input using SpeechRecognition
* 🔊 Respond using text-to-speech with pyttsx3
* 👋 Greet the user when they say "Hello"
* 🕒 Tell the current time
* 📅 Tell today's date
* 🌐 Perform Google searches using voice commands
* ⚠️ Gracefully handle speech recognition errors

### Advanced Features

* 🧠 Natural Language Understanding (NLP) for intent recognition
* 📧 Send emails using voice commands
* ⏰ Set timed reminders with audible alerts
* 🌤️ Retrieve live weather information from OpenWeatherMap
* 📚 Answer general knowledge questions
* ⚙️ Load custom commands from a configuration file
* 🔒 Privacy-aware design with documented data handling

---

## 🛠️ Tech Stack

* Python 3.12+
* SpeechRecognition
* pyttsx3
* datetime
* webbrowser
* requests
* smtplib
* threading
* NLTK or Transformers (for NLP)
* OpenWeatherMap API

---

## 📂 Project Structure

```text
voice-assistant/
│
├── main.py
├── assistant.py
├── config.py
├── commands.json
├── requirements.txt
├── README.md
│
├── services/
│   ├── speech.py
│   ├── tts.py
│   ├── weather.py
│   ├── email_service.py
│   ├── reminder.py
│   ├── browser.py
│   └── knowledge.py
│
├── nlp/
│   └── intent.py
│
├── utils/
│   └── helpers.py
│
└── tests/
    ├── test_speech.py
    ├── test_weather.py
    ├── test_email.py
    └── test_intent.py
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
```

### Create a virtual environment

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
python main.py
```

The assistant will initialize the microphone and begin listening for commands.

---

## 💬 Example Voice Commands

* "Hello"
* "What time is it?"
* "What's today's date?"
* "Search Python tutorials"
* "What's the weather today?"
* "Send an email"
* "Remind me in 15 minutes to drink water"
* "Who invented Python?"
* "Open GitHub"

---

## 🌤️ Weather API Setup

1. Create a free OpenWeatherMap account.
2. Generate an API key.
3. Store the API key securely (for example, in an environment variable or a local `.env` file).
4. Configure the application to read the key before making weather requests.

---

## 📧 Email Configuration

Configure a test email account before using the email feature.

Store credentials securely and never commit passwords or API keys to GitHub.

---

## 🧪 Running Tests

Run all tests:

```bash
pytest
```

Or using unittest:

```bash
python -m unittest discover
```

---

## 🔒 Privacy Considerations

This application is designed with privacy in mind.

* Voice is processed only after the microphone is activated.
* Voice recordings are not permanently stored unless this functionality is explicitly added.
* Weather requests send only the information required to retrieve forecasts.
* Email credentials should be stored securely using environment variables or a local `.env` file.
* Sensitive configuration files should be excluded from version control using `.gitignore`.

---

## 📈 Future Improvements

* Wake word detection (e.g., "Hey Assistant")
* Smart home integration
* Calendar integration
* Voice authentication
* Multi-language support
* Offline speech recognition
* AI-powered conversation using Large Language Models
* Desktop graphical user interface
* Speech history stored in SQLite

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your fork.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Zinhle Sibisi**

Software Engineering Student | Cloud Engineering Enthusiast | Python & Java Developer

Passionate about building practical software solutions while continuously learning backend development, cloud technologies, artificial intelligence, and software engineering best practices.
