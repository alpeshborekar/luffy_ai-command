import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize text-to-speech engine
voice_engine = pyttsx3.init('sapi5')
voice_list = voice_engine.getProperty('voices')
voice_engine.setProperty('voice', voice_list[0].id)

def speak_text(text):
    voice_engine.say(text)
    voice_engine.runAndWait()

def greet():
    hour_now = int(datetime.datetime.now().hour)
    if 0 <= hour_now < 12:
        speak_text("Good Morning!")
    elif 12 <= hour_now < 18:
        speak_text("Good Afternoon!")
    else:
        speak_text("Good Evening!")
    speak_text("I am luffy. How can I assist you today?")

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio_data = recognizer.listen(mic)
    try:
        print("Recognizing...")
        user_command = recognizer.recognize_google(audio_data, language='en-in')
        print(f"User said: {user_command}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return "None"
    except sr.RequestError:
        print("Sorry, there was an issue with the request.")
        return "None"
    return user_command

def send_email(to_email, body):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('youremail@gmail.com', 'your-password')
    smtp.sendmail('youremail@gmail.com', to_email, body)
    smtp.close()

if __name__ == "__main__":
    greet()
    while True:
        command = get_command().lower()
        if 'wikipedia' in command:
            speak_text('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            summary = wikipedia.summary(command, sentences=2)
            speak_text("According to Wikipedia")
            print(summary)
            speak_text(summary)
        elif 'youtube' in command:
            webbrowser.open("https://youtube.com")
        elif 'google' in command:
            webbrowser.open("https://google.com")
        elif 'stackoverflow' in command:
            webbrowser.open("https://stackoverflow.com")
        elif 'play music' in command:
         
            spotify_url = "https://open.spotify.com/episode/2TMQnX2sDj3G77TDIg5xxU?si=d232deb7435242d6"
            webbrowser.open(spotify_url)
            speak_text("Opening your music playlist on Spotify.")
        elif 'current time' in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak_text(f"The current time is {current_time}")
        elif 'open code editor' in command:
            code_path = "C:\\Users\\alpes\\.vscode\\Code.exe"
            os.startfile(code_path)
        elif 'email to alpesh' in command:
            try:
                speak_text("What would you like to include in the email?")
                email_body = get_command()
                recipient_email = "alpeshyourEmail@gmail.com"
                send_email(recipient_email, email_body)
                speak_text("The email has been sent successfully!")
            except Exception as e:
                print(e)
                speak_text("Sorry, I could not send the email.")
        else:
            print("Command not recognized.")
