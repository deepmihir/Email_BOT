"""
Email BOT 
----------------------------------------
This is my simple email bot that interact with you with voice and listen to you.
!! Note !!
if you want to use this bot you need give permission to your google account.
you need to import speech_recognition, PyAudio, pyttx
"""

import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):

    engine.say(text)
    engine.runAndWait()



def get_info():
    try:

        with sr.Microphone() as source:
            print('listening to you...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

email_list ={
    'dip' or 'deep': 'deepmihir@gmail.com'

}



def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('alltechdeep@gmail.com','dk@1532@')
    email = EmailMessage()
    email['From'] = 'alltechdeep@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email')
    subject = get_info()
    talk('Tell me the content of your email')
    message = get_info()
    send_email(receiver, subject,message)



get_email_info()