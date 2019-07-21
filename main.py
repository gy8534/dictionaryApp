import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        print("Did you mean - \"%s\"" % get_close_matches(word, data.keys())[0])
        c = input("Enter Y or N: ")
        if c.lower()=="y":
            return data[get_close_matches(word, data.keys())[0]]
        elif c.lower()=="n":
            return "This word doesn't exist, Please check it"
        else:
            return "You havn't entered a valid choice, Please try again"
    else:
        return "This word doesn't exist, Please check it"

w = input("Enter the Word: ").lower()

m = meaning(w)
print(m)
