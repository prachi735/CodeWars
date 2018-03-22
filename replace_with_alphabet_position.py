from string import ascii_uppercase
from string import ascii_lowercase
from collections import OrderedDict
def alphabet_position(text):
    upper_alpha = dict((k, i+1) for i,k in enumerate(ascii_uppercase))
    lower_alpha = dict((k, i+1) for i,k in enumerate(ascii_lowercase))
    for a in text:
        if a in ascii_uppercase:
            text = text.replace(str(a),str(upper_alpha[a])+" ")
        elif a in ascii_lowercase:
            text = text.replace(str(a),str(lower_alpha[a])+" ")
        elif a == " ":
            pass
        else:
            text = text.replace(str(a),"")
        text = text.replace("  "," ")
        text = text.strip()
    return text
