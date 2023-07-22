class Solution:
    def myAtoi(self, s: str) -> int:
        number_maior = 2 ** 31 - 1
        number_menor = -2 ** 31
        s = s.strip()
        if not s:
            return 0

        sinal = -1 if s[0] == "-" else 1
        if s[0] in ['+', "-"]:
            s = s[1:]

        number = 0
        for letter in s:
            if not letter.isdigit():
                break

            number = number * 10 + (ord(letter) - ord("0"))
            if sinal * number > number_maior:
                return number_maior

            elif sinal * number < number_menor:
                return number_menor

        return sinal * number






solution = Solution()
solution.myAtoi("4193 with words")




