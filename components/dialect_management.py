from abc import ABC, abstractmethod
from flask import flash
import speech_recognition as sr

from components.dialect import Dialect

class DialectManagement(ABC):
    
    @abstractmethod
    def detectDialect(self, audioInput) -> Dialect:
        recognizer = sr.Recognizer()

        with sr.Audio(audio) as audio:
            try:
                audio_data = recognizer.record(audio)
                detected_text = recognizer.recognize_google(audio_data)
                return detected_text
            except sr.UnknownValueError:
                flash("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                flash(f"Could not request results from Google Speech Recognition service; {e}")

    @abstractmethod
    def applyDialectRules(self, dialect: Dialect):
        pass