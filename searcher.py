import urllib.request, json
import _pickle as cPickle
import sys
import math
import pyperclip
import os 
import pyautogui
import winsound


changeID = ""
baseLink = "http://www.pathofexile.com/api/public-stash-tabs?id="
newestStash = ""

snipeItems = []
close = ""

def pause():
    programPause = input("Item found and copied to clipboard \nPress <ENTER> to continue sniping\n")

def sendWhisper():
    pyautogui.press("enter")
    pyautogui.keyDown("ctrl")
    pyautogui.press("v")
    pyautogui.keyUp("ctrl")
    pyautogui.press("enter")
    
    
print("Path of Exile Item Sniper")
print("Enter '5' to end list and start sniping")
while (close != "5"):
    close = input("Enter an item to snipe: ")
    snipeItems.append(close)
   
with urllib.request.urlopen("http://poe-rates.com/actions/getLastChangeId.php") as url:
    data = json.loads(url.read())
    changeID = (data['changeId'])

newestStash = baseLink + changeID
    
with urllib.request.urlopen(newestStash) as stashApi:
    print (stashApi)
    massJson = json.loads(stashApi.read())
    dict = cPickle.dumps(massJson)
    print (str(round(((sys.getsizeof(dict))/1048576),2)) + "mb")

for x in massJson['stashes']:
    for y in x['items']:
        if ('note' in y and 'typeLine' in y and y['typeLine'] != "" and y['note'] != ""):
            for itemName in snipeItems:
                if(itemName in y['typeLine']):
                    print (x['accountName'] + " - " +y['typeLine'] + " - " + y['note'])
                    toClip = "@%s Hi I would like to buy your %s listed for %s" %(x['accountName'], y['typeLine'], y['note'])
                    pyperclip.copy(toClip)
                    winsound.Beep(800, 200)
                    pause()
            
print("Script End")

# To do, make script take change ID from json instead of the website. 
#        refractor into funcions before it ends up a total mess
