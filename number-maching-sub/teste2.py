s = "abcde"
words = ["a", "bb", "acd", "ace"]
string = ""
posicao = -1
match = False
contador = 0
for i in range(len(words)):
    for j in range(len(words[i])):
        index = s.find(words[i][j])
        if index != -1:
            if posicao < index:
                string += words[i][j]
                posicao = index

            else:
                break

        else:
            break

    if string == words[i]:
        contador += 1

    string = ""
    posicao = -1

print(contador)







