#Simple spam bot made by meTju
#Gimme a star on github
#Use at your own risk
import pyautogui
import time
import keyboard
import random
import pyperclip

#Default interval between messages 
interval = 0.1

def send(msg,x):
    pyautogui.typewrite(msg,x)
    pyautogui.press('enter')

def menu():
    print("\nChoose your option:")
    print("1 - Mention spam someone on discord")
    print("2 - Spam with one message")
    print("3 - Spam with text from file")
    print("4 - Settings")
    print("5 - Exit\n")
    print("Option: ",end="")

def spam(msg,include_at=False):
    global interval
    while keyboard.is_pressed('q'):
        if include_at:
            pyautogui.press('enter')
            pyperclip.copy("@")
            pyautogui.hotkey('ctrl', 'v')
        time.sleep(random.uniform(interval,interval*2))
        send(msg,random.uniform(interval,interval*2))
        time.sleep(random.uniform(interval,interval*2))

def settings():
    global interval
    print("Change interval on spams.")
    print("Current interval: ",interval)
    print("Do you want to make change? (y/n): ",end="")
    change = input()

    if change == "y":
        print("Enter new interval: ",end="")
        interval = float(input())
        print("Interval changed to ", interval)

#Main
print("Simple spambot made by meTju")
menu()
option = int(input())
count = 0

while option != 5:
    if option == 1:
        name = input("Enter name of person to spam (@name,@everyone,@here...): ")
        print("Spamming in 8 seconds. Please switch to chat box")
        time.sleep(8)
        spam(name,True)

    elif option == 2:
        message = input("Enter message to spam: ")
        print("Spamming in 8 seconds. Please switch to chat box")
        time.sleep(8)
        spam(message)

    elif option == 3:
        try:
            with open("message.txt","r",encoding='utf-8') as file:
                print("Spamming in 8 seconds. Please switch to chat box")
                time.sleep(8)
                line = file.readline()
                if line:
                    spam(line)
                else:
                    print("File is empty")
        except FileNotFoundError:
            print("File not found")
        except IOError:
            print("Error reading file") 

    else:
        print("Invalid option")
        time.sleep(1)
    
    menu()
    option = int(input())

print("Exiting...")
time.sleep(0.5)