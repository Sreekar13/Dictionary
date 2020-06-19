import json
import difflib

data=json.load(open("/Users/sreekarreddyvelayudham/Documents/PythonProjects/Dictionary/data.json"))

def translator(word):
    if word in data:
        return data[word]
    else :
        recommend=difflib.get_close_matches(word,data.keys(),n=1)
        word=recommend[0] if recommend else ''
        if(word):
            print("Did you mean",word+"?","Yes/No?")
            if(input("Choice: ").lower().startswith(("y","yes"))):
                return data[word]
            else:
                return "The word doesn't exist."
        else:
            return "Please check the word!"

inp=input("Enter the word: ")

result=translator(inp.lower())

if (type(result)!=list):
    print(result)
else:
    for i in result:
        print(i)
