import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Initialize the recognizer, translator, and text-to-speech engine
recognizer = sr.Recognizer()
translator = Translator()
engine = pyttsx3.init()

# Function to recognize speech
def recognize_speech(language="en"):
    with sr.Microphone() as source:
        print(f"Listening in {language}...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
            print("Audio captured.")
            text = recognizer.recognize_google(audio, language=language)
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None

# Function to translate the recognized text
def translate_text(text, target_language="es"):
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Function to speak the translated text
def speak_text(text, language="en"):
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
    engine.setProperty('language', language)
    engine.say(text)
    engine.runAndWait()

# Function to facilitate real-time conversation
def real_time_conversation():
    while True:
        print("English Speaker's turn:")
        english_text = recognize_speech("en")
        if english_text:
            print(f"Translating to Spanish: {english_text}")
            spanish_translation = translate_text(english_text, target_language="es")
            print(f"Spanish Translation: {spanish_translation}")
            speak_text(spanish_translation, language="es")  # Speak the translated Spanish text

        print("Spanish Speaker's turn:")
        spanish_text = recognize_speech("es")
        if spanish_text:
            print(f"Translating to English: {spanish_text}")
            english_translation = translate_text(spanish_text, target_language="en")
            print(f"English Translation: {english_translation}")
            speak_text(english_translation, language="en")  # Speak the translated English text

# Run the conversation loop
real_time_conversation()
