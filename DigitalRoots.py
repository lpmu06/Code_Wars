# Soma todos os dígitos de um dado número, se essa soma tiver mais de 1 dígito, repetir a ação

def digital_root(n):
    list_n = []
    soma_atual = 0

    # Transformando o número em lista, pega o formato string de n, e para cada dígito em n, adicionar o dígito em n_list
    for i in str(n):
        list_n.append(int(i))
        print(list_n)
    # ifzin para resolver o problema que eu criei no while =D
    if len(list_n) == 1:
        soma_atual = list_n[0]
    else:
        # Enquanto o tamanho da lista for maior que 1 repetir loop:
        while len(list_n) > 1:
            # print(f"Lista atual: {list_n}")
            soma_atual = 0  # Reseta soma_final, para receber a lista atual
            for i in list_n:
                soma_atual = soma_atual + i  # Para cada item na lista, somar aquele item no valor total soma_final
            list_n = []  # Zera a lista, senão no futuro ela irá receber valores infinitamente
            for i in str(soma_atual):  # Para cada dígito na soma atual, adicionar o dígito em n_list
                list_n.append(int(i))
            print(f"A soma é: {soma_atual}")

    # O pulo do gato na minha dificuldade (listas ou somas infinitas) foi fazer um ping-pong com os valores dos dígitos
    # Tal hora zerando a lista e passando pra soma, tal hora zerando a soma e passando para a lista.

    # Mais um problema, o meu while servia para listas com mais de 1 valor, com exatamente len[1], ela ignorava, meti um if

    return soma_atual


print(digital_root(8))
