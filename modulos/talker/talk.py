import io
from pydub import AudioSegment
import speech_recognition as sr
import os
import pyttsx3


class TtsTalker:
    def __init__(self):
        self.engine = pyttsx3.init()        
        self.engine.setProperty('rate', 145)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


class Talker:
    def __init__(self, talker_cls):
        self.talker_cls = talker_cls
        
    def talk(self, text):
        self.talker_cls.talk(text)
