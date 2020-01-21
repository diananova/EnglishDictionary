import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:     #for words that start with a capital letter, ex. Paris
        return data[w.title()]
    elif w.upper() in data:     #for acronyms like NATO
        return data[w.upper()]
    #get_close_matches("rainn", ["rain", "pyramid", "love"])
    elif len(get_close_matches(w, data.keys(), n=3)) > 0: 
        i = 0
        while i != 3:  #max number of similar matches
            yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[i])
            if yn == "Y":
                return data[get_close_matches(w, data.keys())[0]]
            elif yn == "N":
                i=i+1
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
