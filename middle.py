def spin_words(sentence):
    words = sentence.split(' ')
    result = ''
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
            result = f'{result} {word}'
        else:
            result = f'{result} {word}'
            
    return result[1:]

print(spin_words('hey coder warrior'))



def spin_words2(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)