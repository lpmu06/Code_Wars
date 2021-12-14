"""
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
"""

def get_count(sentence):
    vowel_num = 0
    sentence = sentence.lower()  # coloquei isso pq né... sempre bom, mas no desafio deixa explícito ser minúsculo.
    for char in sentence:
        if char in "aeiou":
            vowel_num += 1
    return vowel_num

print(get_count("oi, eu sou dollynho, o seu amiguinho"))
