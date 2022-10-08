"""
Made by Arpit Sengar
"""


import speech_recognition as sr
import pyttsx3
from pyautogui import*

r = sr.Recognizer()

def SpeakText(command):

    engine = pyttsx3.init()
    
    engine.say(command)
    engine.runAndWait()
def count_down()
    SpeakText("5")
    write('.', interval = 0.25)
    SpeakText("4")
    write('.', interval = 0.25)
    SpeakText("3")
    write('.', interval = 0.25)
    SpeakText("2")
    write('.', interval = 0.25)
    SpeakText("1")


print('Loading')
write('....', interval = 1)
SpeakText('How can i help you')
print('How can i help you')


while(1):
    
 
    try:
        
        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
     
            
            if MyText == "i want to hear a song" or MyText == 'song' or MyText == "play a song" or MyText == "play song" or MyText == "mujhe ek gana sunna hai" :
                                                    SpeakText('Okay what song would you like to hear?')
                                                    print("Okay what song would you like to hear?")
                                                    audio2 = r.listen(source2)            
                                                    MySong = r.recognize_google(audio2)
                                                    MySong = MySong.lower()
                                                    keyDown('win')
                                                    press('r')
                                                    keyUp('win')
                                                    write('brave')
                                                    press('enter', interval = 3)
                                                    write('https://www.youtube.com', interval = 0.1)
                                                    press('enter', interval = 4)
                                                    press('/')                                                    
                                                    x = MySong + ' song'
                                                    write(x, interval = 0.1)
                                                    press('enter', interval = 3)
                                                    click(x=300, y= 300, button = 'left')

                                                               

            elif MyText == "decrease the volume" or MyText == "decrease the volume":
                                                    SpeakText("Decreasing the volume by 20")
                                                    print("Decreasing the volume by 20")
                                                    for i in range(11):
                                                        press('volumedown')


            elif MyText == "increase the volume" or MyText == "increase the volume:
                                                    SpeakText("Increasing the volume by 20")
                                                    print("Increasing the volume by 20")
                                                    for i in range(11):
                                                        press('volumeup')


            elif MyText == "mute the volume" or MyText == "mute the volume":
                                                    SpeakText("Volume muted")
                                                    print("Volume muted")
                                                    press('volumemute')

                                                
            elif MyText == "unmute the volume" or MyText == "unmute the volume":
                                                    SpeakText("Volume unmuted")
                                                    print("Volume unmuted")
                                                    press('volumemute')

            
            elif MyText == "go to the home screen" or MyText == "home screen":                              
                                                    keyDown('win')
                                                    press('d')
                                                    keyUp('win')

            
            elif MyText == "switch tabs " or MyText == "switch tabs":
                                                    SpeakText("Switching tabs")
                                                    print("Switching Tabs")
                                                    keyDown('alt')
                                                    press('tab')
                                                    keyUp('alt')


            elif MyText == "create a desktop" or MyText == "create a desktop " or MyText == "create desktop":
                                                    SpeakText("Creating a desktop")
                                                    print("Creating a desktop")
                                                    keyDown('win')
                                                    keyDown('ctrl')
                                                    press('d')
                                                    keyUp('ctrl')
                                                    keyDown('win')

                                                    
            elif MyText == "close all the desktops" or MyText == "close all desktops " or MyText == "close all desktops" or MyText == "close desktops": 
                                                    for i in range(10):
                                                        keyDown('win')
                                                        keyDown('ctrl')
                                                        press('f4')
                                                        keyUp('ctrl')
                                                        keyDown('win')
                                                    SpeakText("all desktops deleted successfully")
                                                    print("All desktops deleted successfully")
                                                    
                                                    
            elif MyText == "minimise":
                                                    print("Window minimized.")
                                                    keyDown('win')
                                                    press('down')
                                                    keyUp('win')

                                                    
            elif MyText == "close this application" or MyText == "close application" :
                                                    print("Closing an application")
                                                    keyDown('alt')
                                                    press('f4')
                                                    keyUp('alt')


            elif MyText == "show me the left desktop" or MyText == "left desktop" or MyText == "left screen":
                                                    keyDown('win')
                                                    keyDown('ctrl')
                                                    press('left')
                                                    keyUp('ctrl')
                                                    keyDown('win')


            elif MyText == "show me the right desktop" or MyText == "right desktop" or MyText == "right screen":
                                                    keyDown('win')
                                                    keyDown('ctrl')
                                                    press('right')
                                                    keyUp('ctrl')
                                                    keyDown('win')


            elif MyText == "shut down":
                                                    SpeakText("shutting down in")
                                                    count_down()
                                                    keyDown('win')
                                                    press('d')
                                                    keyUp('win')
                                                    keyDown('alt')
                                                    press('f4')
                                                    keyUp('alt')
                                                    press('enter')

                
            elif MyText == 'restart' or MyText == 'reboot':
                                                    SpeakText("rebooting in")
                                                    count_down()
                                                    keyDown('win')
                                                    press('d')
                                                    keyUp('win')
                                                    keyDown('alt')
                                                    press('f4')
                                                    keyUp('alt')
                                                    press('down')
                                                    press('enter')                               

            
            elif MyText == 'refresh':
                                                    keyDown('win')
                                                    press('d')
                                                    keyUp('win')
                                                    for i in range(2):
                                                        keyDown('fn')
                                                        press('f5')
                                                        keyUp('fn')
                                                

            elif MyText == 'maximum volume':
                                                    for i in range(50):
                                                        press('volumeup')
                                                        

            elif MyText == 'enter' or MyText == 'press enter':
                                                    press('enter')
                                                    
                                                                                                     
            else:
                print("Sorry i could not understand that ")
                SpeakText("Sorry i could not understand that")
                            
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("******")
    
