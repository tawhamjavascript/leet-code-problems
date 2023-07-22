produtos, negado = list(map(int, input().split()))
array_negado = [list(map(int, input().split())) for i in range(negado)]
array_produtos = [i + 1 for i in range(produtos)]
combinacao = []


def comb(v, n, v0 = []):
    if n == 1:
        for i in range(len(v)):
            array = v0 + [v[i]]
            combinacao.append(array)
    else:
        for i in range(produtos - n + 1):
            array = v0 + [v[i]]
            if array not in array_negado:
                comb(v[i + 1:], n - 1, array)


comb(array_produtos, 2)
