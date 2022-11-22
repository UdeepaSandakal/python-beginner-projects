import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif (len(get_close_matches(w, data.keys())) > 0):
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(w, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist.P;ease double check it."
        else:
            return "Your entry is wrong"
    else:
        return "The word doesn't exist.Plea se double check it."

word = input("Enter word: ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print("\n"+item)
else:
    print(output)