
import pyautogui
from time import sleep
from random import randint

print("Enter How many messages")
x =int(input())  #how many messages or comments you want to send

def name():
    """generates random names"""

    nameList = ["babe","babe","babe"]   #list of names (change according to your requirement)
    rand_name = nameList[randint(0, len(nameList) - 1)]      #traverse names randomly for n, from 0 to (n-1)

    return rand_name    #return the random name it just generated
 


while True:      #forever loop
    pyautogui.typewrite(f" {name()}")  #type message
    sleep(.600)                        #A bit delay of 600 ms
    pyautogui.typewrite("\n")          #New line, here 'Enter' to send text
    sleep(.1000)                           #delay of 2 seconds

    x = x - 1         #decrement x value by 1

    if x == 0:       
        break         #get out of the loop and finish
