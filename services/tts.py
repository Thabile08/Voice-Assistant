import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

        # Optional settings
        self.engine.setProperty("rate", 170)    # Speed of speech
        self.engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

    def speak(self, text):
        """Convert text to speech."""
        self.engine.say(text)
        self.engine.runAndWait()