import openai
import os
import pyttsx3
import pyaudio
import wave
import json


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "pregunta.wav"

# Configura tu clave de API
openai.api_key = ""

audio = pyaudio.PyAudio()

# Configuramos la grabación de audio
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

print("Grabando...")

frames = []

# Grabamos el audio
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Grabación finalizada.")

# Paramos la grabación y cerramos el flujo
stream.stop_stream()
stream.close()
audio.terminate()

# Guardamos el audio en un archivo WAV
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

audio_file = open("pregunta.wav", "rb")
transcript = openai.Audio.transcribe ("whisper-1", audio_file)

cadena_json = json.dumps (transcript)

objeto_python = json.loads(cadena_json)

prompt = objeto_python['text']

# Configura los parámetros de la solicitud
model_engine = "text-davinci-002"
max_tokens = 500

# Envía la solicitud a la API de OpenAI
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens
)

# Imprime la respuesta de GPT-3.5
#print(response.choices[0].text.strip())

engine = pyttsx3.init()
voices = engine.getProperty('voices') 

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 160)     # setting up new voice rate
engine.setProperty('voice', voices[0].id)  
engine.say(response.choices[0].text.strip())
engine.runAndWait()

#Revisar voice.language <- hay opción para español o debería.
#https://github.com/nateshmbhat/pyttsx3
