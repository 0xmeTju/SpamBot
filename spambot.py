#Simple spam bot made by meTju
#Gimme a star on github: https://github.com/I-meTju-I
#Made for educational purposes. Use at your own risk
import pyautogui
import time
import keyboard
import random
import pyperclip
import os

#Default interval between messages 
interval = 0.1

def send(msg,delay):
    pyautogui.typewrite(msg,delay)
    pyautogui.press('enter')

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(''' ___  ____   __    __  __  ____  _____  ____ 
/ __)(  _ \ /__\  (  \/  )(  _ \(  _  )(_  _)
\__ \ )___//(__)\  )    (  ) _ < )(_)(   )(  
(___/(__) (__)(__)(_/\/\_)(____/(_____) (__) by meTju''')
    print('''DISCLAIMER: When you choose the spam option, an 8-second timer starts. Move your cursor to the appropriate chat box. 
Pause spamming anytime by holding the 'ESC' key. More info in README.\n''')
    print("\nChoose your option:")
    print("1 - Mention spam someone on Discord")
    print("2 - Spam with one message")
    print("3 - Spam with text from file")
    print("4 - Settings")
    print("5 - Exit\n")
    print("Option: ",end="")

def spam(msgs,include_at=False):
    global interval
    while True:
        if include_at:
            pyautogui.press('enter')
            pyperclip.copy("@")
            pyautogui.hotkey('ctrl', 'v')
        for msg in msgs:
            if keyboard.is_pressed("esc"):
                print("Spamming terminated. Returning...")
                time.sleep(2)
                return
            time.sleep(random.uniform(interval,interval*2))
            send(msg,random.uniform(interval/6,interval/3))
            time.sleep(random.uniform(interval,interval*2))

def settings():
    global interval
    print("Change the interval between spams.")
    print("Current interval: ",interval)
    print("Do you want to make change? (y/n): ",end="")
    change = input()

    if change == "y":
        print("Enter the new interval: ",end="")
        interval = float(input())
        print("Interval changed to: ", interval)
        time.sleep(1)

def input_option():
    while True:
        try:
            option = int(input())
            return option
        except ValueError:
            print("Invalid option...")
            time.sleep(1)
            menu()
            continue

#Main
menu()
option = input_option()
count = 0

while option != 5:
    if option == 1:
        name = input("Enter the name of person to spam on Discord(@name, @everyone, @here...): ")
        print("Spamming in 8 seconds. Switch to the chat box")
        time.sleep(8)
        spam([name],True)

    elif option == 2:
        message = input("Enter the message to spam: ")
        print("Spamming in 8 seconds. Switch to the chat box")
        time.sleep(8)
        spam([message])

    elif option == 3:
        try:
            with open("message.txt","r",encoding='utf-8') as file:
                buffer = file.readlines()
                buffer = [msg.strip() for msg in buffer]
                if buffer:
                    print("Spamming from file in 8 seconds. Switch to the chat box")
                    time.sleep(3)
                    spam(buffer)
                else:
                    print("File is empty...")
                    time.sleep(2)

        except FileNotFoundError:
            print("File not found...")
            time.sleep(2)
        except IOError:
            print("Error reading file...")
            time.sleep(2)

    elif option == 4:
        settings()

    else:
        print("Invalid option...")
        time.sleep(1)
    
    menu()
    option = input_option()

print("Exiting...")
time.sleep(0.5)