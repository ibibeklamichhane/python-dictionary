import json
import difflib
from difflib import get_close_matches


data=json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) >0:
        yn=input("Did you mean %s  instead? Enter y for yes and n for no" %get_close_matches(w,data.keys)[0])
        if yn=="y":
            return  data[get_close_matches(w,data.keys()[0])]
        elif yn =='n':
            return "sorry the words doesnt exist"
    else:

        return " sorry the word doesnt exist!!!"


word=input("enter your words")

print(translate(word))
