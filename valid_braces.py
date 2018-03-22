def validBraces(string):
    opening_p = ['(','{','[']
    closing_p = [')','}',']']
    p1 = opening_p + closing_p
    p2 = closing_p + opening_p
    braces = []
    l = len(string)
    for s in string:
        if len(braces) == 0:
            braces.append(s)
        elif p1.index(braces[len(braces)- 1]) == p2.index(s) and braces[len(braces)- 1] in opening_p and s in closing_p:
            braces.pop()
        else:
            braces.append(s)
    if len(braces) == 0:
        return True
    else:
        return False
