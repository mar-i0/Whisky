import requests
import wave
import pyaudio
import urllib.parse
import pygame
import random
import openai
import os
import pyttsx3
import json



def reproducir_audio(texto):
    #texto_url = urllib.parse.quote(texto)
    url = "https://www.google.com/speech-api/v2/synthesize"
    params = {
        "enc": "mpeg",
        "client": "chromium",
        "key": "AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw",
        "text": texto,
        "lang": "es-ES",
        "speed": "0.5",
        "pitch": "0.3"
    }
    
    #sound_obj = playsound("luces4.mp3")
    
    pygame.init()

    luces_sound = pygame.mixer.Sound("luces4.mp3")
    luces_sound.play()
    pygame.time.wait(int(luces_sound.get_length() * 1000))


    response = requests.get(url, params=params)
    with open("respuesta.mp3", "wb") as f:
        f.write(response.content)
    f.close

    respuesta_sound = pygame.mixer.Sound("respuesta.mp3")
    respuesta_sound.play()
    pygame.time.wait(int(respuesta_sound.get_length() * 1000))

    pygame.quit()




def aleatorio():

    opcion = random.randint(1,19)
    if opcion == 1:
        reproducir_audio("Mi carrocería está fabricada con una aleación de alta resistencia y mi blindaje es capaz de soportar cualquier impacto.")
    elif opcion == 2:
        reproducir_audio("Soy la voz del microprocesador de Knight Industrias 2023.")
    elif opcion == 3:
        reproducir_audio("¡Soy la I.A. más sofisticada y tecnológicamente avanzada del mundo!.")
    elif opcion == 4:
        reproducir_audio("No solo soy una I.A., soy un amigo.")
    elif opcion == 5:
        reproducir_audio("Mi función es protegerte a toda costa.")
    elif opcion == 6:
        reproducir_audio("¡No me quemes la tapicería!.")
    elif opcion == 7:
        reproducir_audio("Soy KITT, un sistema de transporte inteligente y microprocesado.")
    elif opcion == 8:
        reproducir_audio("No tengo la capacidad de ser irónico.")
    elif opcion == 9:
        reproducir_audio("¿Estás seguro de que deberíamos estar haciendo esto?.")
    elif opcion == 10:
        reproducir_audio("No te preocupes, siempre tengo un plan.")
    elif opcion == 11:
        reproducir_audio("¿Qué tal si ponemos el turbo y dejamos a estos tipos atrás?.")
    elif opcion == 12:
        reproducir_audio("¿podrías ir un poco más despacio? ¡Me estoy mareando!.")
    elif opcion == 13:
        reproducir_audio("La velocidad máxima no lo es todo.")
    elif opcion == 14:
        reproducir_audio("¡No siempre necesitas una I.A. para resolver tus problemas!.")
    elif opcion == 15:
        reproducir_audio("No te preocupes, siempre estoy aqui para ayudarte.")
    elif opcion == 16:
        reproducir_audio("¡Atención!, detecto peligro en la zona.")
    elif opcion == 17:
        reproducir_audio("¡Por supuesto! Mi capacidad de análisis de datos es superior a la de cualquier ser humano")
    else :
        reproducir_audio("No te preocupes, ¡Siempre existe una solución!")
    
        

def preguntar_a_gpt():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "pregunta.wav"

    # Configura tu clave de API AQUI
    # Configura tu clave de API AQUI
    # Configura tu clave de API AQUI
    # Configura tu clave de API AQUI
    # Configura tu clave de API AQUI
    openai.api_key = ""
    # Configura tu clave de API AQUI
    # Configura tu clave de API AQUI


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
    aleatorio()
    reproducir_audio(response.choices[0].text.strip())



preguntar_a_gpt()

                 




