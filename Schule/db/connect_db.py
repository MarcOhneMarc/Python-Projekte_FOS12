sentence = "ich teste"

def spinWords(sentence):
    words = sentence.split(' ')
    l = []
    for word in words:
        if len(word) >= 5:
            l.append(word[::-1])
        else:
            l.append(word)
    print(' '.join(l))


spinWords(sentence)
