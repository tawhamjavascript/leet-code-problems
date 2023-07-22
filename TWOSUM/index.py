lista, target = [input() for i in range(2)]
target = int(target)
array = list()
condicao = ["[", "]", ","]
for i in range(len(lista)):
    if lista[i] not in condicao:
        array.append(int(lista[i]))


def funcao():
    apontadorA = 0
    apontadorB = 0
    fim = len(array)
    while True:
        if apontadorA == fim:
            print("Não existe")
            break 

        elif apontadorB == fim:
            apontadorA += 1
            apontadorB = apontadorA

        elif apontadorA == apontadorB:
            if array[apontadorA] == target:
                return [apontadorA, apontadorB]

        else:
            if array[apontadorA] + array[apontadorB] == target:
                return [apontadorA, apontadorB]
        
        apontadorB += 1

funcao()




 

