import io #Trabajar con archivos para guardar y manipular
from pydub import AudioSegment #Tomar el audio y volverlo un archivo temporal
import speech_recognition as sr  #Reconoce el audio
import whisper  #Motor del Asistente
import tempfile  #Generar archivos temporales
import os  #Sistema Operativo
import pyttsx3  #Generar voz

#C:\Users\jumay\Desktop\VirtualAssistant>.\venv\Scripts\activate

temp_file = tempfile.mkdtemp()
save_path = os.path.join(temp_file, 'temp.wav')

listener = sr.Recognizer()

class Listener:
    def __listen_from_mic(self):
        try:
            with sr.Microphone() as source:
                print("Escuchando..........")
                listener.adjust_for_ambient_noise(source)
                audio = listener.listen(source)
                data = io.BytesIO(audio.get_wav_data())
                audio_clip = AudioSegment.from_file(data)
                audio_clip.export(save_path, format='wav')
        except Exception as e:
            print(e)
        return save_path


    def __recognize_audio(self, save_path):
        audio_model = whisper.load_model('base')
        transcription = audio_model.transcribe(save_path, language='spanish', fp16=False)
        return transcription['text']
    
    def listen(self):
        return self.__recognize_audio(self.__listen_from_mic())