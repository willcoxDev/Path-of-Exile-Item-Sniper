import urllib.request, json
import _pickle as cPickle
import sys
import math
import pyperclip
import os

changeID = ""
baseLink = "http://www.pathofexile.com/api/public-stash-tabs?id="
newestStash = ""

snipeItems = []
close = ""

def pause():
    programPause = input("Item found and copied to clipboard \nPress <ENTER> to continue sniping\n")


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
                    pause()
            
        
