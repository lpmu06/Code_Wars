# Esse desafio consiste em pegar os caracteres de uma palavra e transformar em uma strings de ) ou (, aplicando
# "(" no lugar de um caracter se ele apareceu apenas uma vez na palavra, e ")" no lugar daquele caracter que apareceu
# mais de uma vez


def duplicate_encode(word):
    word = word.lower()  # Se for maiúscula ou minúscula afeta.

    # Quem faz a magia é esse set nesse for(if)
    # Set: Set é uma coleção que representa conjunto. Essa coleção tem como
    # caracteristica ser desordenada e ter os elementos únicos, ou seja,
    # não existe repetição de elementos nesse tipo de coleção.
    list_duplicates = list(set([x for x in word if word.count(x) > 1]))

    # Acima: x é a posição de tal letra em uma palavra(word), se o número de vezes que aquela letra aparece na palavra
    # for maior que 1, então ela é adicionada ao set, caso não, roda o for para a letra seguinte.

    encoder_list = []
    encoder_str = ""
    for i in word:
        if i in list_duplicates:
            encoder_list.append(r')')
            print()
        else:
            encoder_list.append(r'(')
            print()

    for x in encoder_list:
        encoder_str += x

    return encoder_str


print(duplicate_encode("LUISI"))

