"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    text_splited = text.split(' ')
    print(text_splited)
    text_pigged = ""
    for word in text_splited:
        if word.isalpha() == False:
            text_pigged += word + " "
        else:
            word = list(word)
            word += word[0]
            word.pop(0)
            word.append('ay')
            #Essa parte abaixo eu tive que pesquisar, deu certo
            # https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python
            word = ''.join([str(item) for item in word])
            print(word)
            text_pigged += word + " "

    return text_pigged[:-1]

print(pig_it('Hello world !'))
