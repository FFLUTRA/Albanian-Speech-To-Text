from abc import ABC, abstractmethod
from flask import flash
import speech_recognition as sr

from enums.dialect import Dialect
from components.dialect_management import DialectManagement

class DialectManagementImpl(DialectManagement):

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


    def applyDialectRules(self, dialect: Dialect):
        return super().applyDialectRules()