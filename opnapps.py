import os
from time import sleep
import pyautogui
import webbrowser
import pygame



def speak(text) :
     voice = 'en-US-EmmaMultilingualNeural'
     text = text.replace("&", "&amp;")
     data = f"python -m edge_tts --rate=+0% --voice \"{voice}\" --text \"{text}\" --write-media \"data.mp3\""
     os.system(data)

     pygame.init()
     pygame.mixer.init()
     pygame.mixer.music.load("data.mp3")

     try:
          pygame.mixer.music.play()

          while pygame.mixer.music.get_busy():
               pygame.time.Clock().tick(10)

     except Exception as e:
          print(e)

     finally:
          pygame.mixer.music.stop()
          pygame.mixer.quit()

opnapps = {"commandprompt":"cmd", "paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openappweb(quary):
     speak(" launching, master")
     if ".com" in quary or ".org" in quary or ".co.in" in quary:
          quary = quary.replace("open","")
          quary = quary.replace("launch","")
          quary = quary.replace("mariya","")
          quary = quary.replace(" ", "" )
          webbrowser.open(f"https://www.{quary}")
     else:
          keys = list(opnapps.keys())
          for app in keys:
               if app in quary:
                    os.system(f"start {opnapps[app]}")

def closewebapp(quary):
     if "one tab " in quary or "1 tab" in quary:
          pyautogui.hotkey("ctrl","w")
     elif "2 tab" in quary:
          pyautogui.hotkey("ctrl", "w")
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          speak("All tabs closed")
     elif "3 tab" in quary:
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          sleep(0.5)
          speak("All tabs closed") 
     elif "4 tab" in quary:
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          speak("All tabs closed") 
     elif "5 tab" in quary:
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          sleep(0.5)
          pyautogui.hotkey("ctrl", "w")
          speak("All tabs closed")
     else:
          keys = list(opnapps.keys())
          for app in keys:
               if app in quary:
                    os.system(f"taskkill /f /im {opnapps[app]}.exe")

