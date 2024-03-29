import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source, None, 10)  # voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'what is the ' in command:
        person = command.replace('what is the', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'do you like to go to the diner with me' in command:
        talk('sorry, I have a headache')
    elif 'good morning ' in command:
        talk('good morning mr.gunawardhana')
    elif 'good afternoon ' in command:
        talk('good afternoon mr.gunawardhana')
    elif 'good evening' in command:
        talk('good evening mr.gunawardhana ')
    elif 'good night' in command:
        talk('good night sweat dreams mr.gunawrdhana ')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'who is mr.gunawardhana ' in command:
        talk('he is in my master')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    try:
        run_alexa()
    except UnboundLocalError:
        print("No command detected! Alexa has stopped working ")
        break
