class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matriz = [[] for i in range(numRows)]
        linha = 0
        contador = 0
        string = ""
        if numRows == 2:
            for letra in s:
                matriz[linha].append(letra)
                linha += 1
                if linha > 1:
                    linha = 0

            for line in matriz:
                string += "".join(line)

        else:
            for letra in s:
                matriz[linha].append(letra)
                if contador % 2 == 0:
                    linha += 1
                    if linha == numRows:
                        linha = numRows - 2
                        contador += 1
                else:
                    linha -= 1
                    if linha < 1:
                        linha = 0
                        contador += 1

            for line in matriz:
                string += "".join(line)

        return string


solution = Solution()
print(solution.convert("ABCDE", 2))
