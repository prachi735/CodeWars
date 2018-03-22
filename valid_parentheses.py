def valid_parentheses(string):
    l = 0
    for s in string:
        if s == '(':
            l = l + 1
        if s == ')':
            l = l - 1
        if l < 0:
            return False
    if l == 0:
        return True
    else:
        return False
