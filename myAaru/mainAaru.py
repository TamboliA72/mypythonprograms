#Program for Aaru
import speech_recognition as sprec
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time
import os
import pyjokes

listner = sprec.Recognizer()
txtToSpeechObj = pyttsx3.init()
voices = txtToSpeechObj.getProperty('voices')
txtToSpeechObj.setProperty('voice', voices[0].id)

#function to respond to the users commands
#input - the text that must be spoken
#output - speech response
def aaruTalk(text):
    txtToSpeechObj.say(text)
    txtToSpeechObj.runAndWait()

#function to greet the user and ask his name
#input - no
#output - returns the user name
def getUserName():
    userName = ""
    try:
        with sprec.Microphone() as spSource:
            print('listening...')
            aaruTalk('Hello!, I am Aaru Your Personal Companion')
            aaruTalk('May I know your name?')
            userSpInput = listner.listen(spSource)
            userName = listner.recognize_google(userSpInput) #to get the username and recognize it using 'recognize_google' function
            userName.lower() #converting the command to lower case so that it will be easy to handle
            print(userName)
			#replacing 'I am' or 'my name is' from the command to get the user name 
            if 'my name is' in userName:
                userName = userName.replace('my name is','')
            elif 'i am' in userName:
                userName = userName.replace('I am','')
    except:
        pass   
    return userName.replace('i am', '')    

#function to listen to the user command having the name 'aaru'
#input - user name
#output - the command for processing 
def aaruTakeCommand(user_name):
    command = ""
    try:
        with sprec.Microphone() as spSource:            
            userSpInput = listner.listen(spSource)                        
            command = listner.recognize_google(userSpInput)
            command = command.lower()
            if 'aaru' in command:
                command = command.replace('aaru', '')
                print(command) #printing the command that is heard
    except:
        txtToSpeechObj.say('Hey '+ user_name +', Please check your mic. I think its not properly working!') #throwing the exception if the command is not properly heard
    return command

#function to listen to the user command
#input - no
#output - returns the command
def aaruListen():
    command = ''
    try:
        with sprec.Microphone() as spSource:
            userInp = listner.listen(spSource)
            command = listner.recognize_google(userInp)
            command = command.lower()
    except:
        pass
    return command

#function to tell the jokes using the pyjoke library
#input - user name
#output - no
def tellJoke(user_Name):
    userInp = ""
    aaruTalk('Okay, here is one')
    joke = pyjokes.get_joke(language="en", category="all")
    aaruTalk(joke)
    time.sleep(2) #waiting for 2 seconds
    aaruTalk('ha ha ha it was really funny!')
    '''while ('yes' or 'yeah') in userInp:
        joke = pyjokes.get_joke(language="en", category="all")
        aaruTalk(joke)
        aaruTalk('do you want to here more?')
        userInp = listner.listen(sprec.Microphone())'''

#function to execute the various commands given by the user
#input - user name
#output - no
def executeAaru(user_Name):
    print('listening...')
    newCommand = aaruTakeCommand(user_Name) #calling 'aaruTakeCommand' function for giving the commands
    print(newCommand)
    if 'play' in newCommand: #for playing the songs on youtube
        song = newCommand.replace('play','')
        aaruTalk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif ('tell joke' or 'joke') in newCommand: #for telling a joke
        tellJoke(user_Name)
    '''elif 'start' in newCommand:
        program = newCommand.replace('start','')
        aaruTalk('Starting ' + program)
        os.subprocess.Popen(r'explorer /select,"C:"')'''
    

#wake_word = "hey aaru"

user_Name = getUserName() #calling the getUserName function for accepting the user name
print(user_Name) #printing the username for debugging

#actual program execution starts from here
while True: #continuous execute the code
    print('listening...')
    command = aaruListen() #calling 'aaruListen' function to give a command
    if 'aaru' in command:
        aaruTalk('Hey ' + user_Name + ', How can I help you?') #calling 'aaruTalk' function to make it talk the response
        executeAaru(user_Name) #calling the 'executeAaru' function to give the different command and execute them