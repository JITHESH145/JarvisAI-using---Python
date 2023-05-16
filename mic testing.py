import speech_recognition as sr

microphone_list = sr.Microphone.list_microphone_names()
for index, microphone_name in enumerate(microphone_list):
    print(f"Device Index: {index}, Microphone Name: {microphone_name}")

# Test each microphone
for index, microphone_name in enumerate(microphone_list):
    try:
        print(f"Testing Microphone {index} ({microphone_name})")
        with sr.Microphone(device_index=index) as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"Recognized text: {text}")
            break  # Stop testing once successful recognition occurs
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except sr.RequestError as e:
        print(f"Error: {e}")
