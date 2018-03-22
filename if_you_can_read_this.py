def to_nato(words):
    #your code here
    new_words = ' '.join([NATO.get(c.upper(),c) for c in words if c != ' '])
    return new_words
