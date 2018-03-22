def spin_words(sentence):
    word_list = sentence.split(' ')
    word_list = [word[::-1]+' ' if len(word) >= 5 else word+' ' for word in word_list]
    return ''.join(word_list).strip()
