import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
#SequenceMatcher(None, "rainn", "rain").ratio()
#get_close_matches(word, list of words)

data = json.load(open("076 data.json", 'r'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, list(data.keys())))>0:
        yn = input( "Did you mean %s instead?" % get_close_matches(word, list(data.keys()))[0])
        if yn.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.lower() == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand what you said! "


    else:
        return "The word doesn't exist. Please double check it! "

userInput = input("Please write your word!")

output = translate(userInput)

if type(output) == list:
    for i in output:
        print(i)



'''

#my implementation
def translate(word):
    word = word.lower()
    try:
        if word in data:
            for i in data[word]:
                print(i)
        else:
            if len(get_close_matches(word, list(data.keys()))) > 0:
                print("Did you mean:")
                for y in get_close_matches(word, list(data.keys())):
                    print(y, end=", ")
    except:
        print("There is no such word in here! ")

userInput = input("Please write your word!")

translate(userInput)
'''
