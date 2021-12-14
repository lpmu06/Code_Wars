"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1
"""


def find_it(seq):
    # Cria um dict usando count, enumerando quantas vezes cada item foi passado lista.
    seq_dict = {i: seq.count(i) for i in seq}
    print(seq_dict.items())
    # Para cada key irá rodar um if perguntando se é ou não impar. Como há obrigatoriamente 1 por lista não há erro.
    for pk, pv in seq_dict.items():
        if pv % 2 == 1:
            return pk


print(find_it([10, 10, 20, 30, 20]))
