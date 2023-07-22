from itertools import combinations


class Solution:

    def numMatchingSubseq(self, s: str, words: 'List[str]') -> int:
        dici = {}
        contador = 0
        for palavra in words:
            result = dici.get(len(palavra))
            if result is None:
                temp = list(combinations(s, len(palavra)))
                dici.update({len(palavra): ["".join(combi) for combi in temp]})
                result = dici.get(len(palavra))

            for combi in result:
                if combi == palavra:
                    contador += 1
                    break

        return contador


solution = Solution()
solution.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"])

