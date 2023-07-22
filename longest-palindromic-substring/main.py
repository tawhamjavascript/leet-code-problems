class Solution:
    def longestPalindrome(self, s: str) -> str:
        biggerSubstring = ""
        max_word = -1
        string = ""
        apontadorInicio = 0
        apontadorFim = 0
        length = len(s)
        if length == 1:
            return s

        elif length == 2:
            return s if s[0] == s[-1] else s[0]


        for i in range(length):
            
















        while True:
            string += s[apontadorFim]
            length_string = (apontadorFim + 1) - apontadorInicio

            if max_word < 1:
                max_word = 1
                biggerSubstring = string

            elif length_string > 1 and string[0] == string[-1]:
                if max_word < 2 and length_string == 2:
                    max_word = 2
                    biggerSubstring = string

                elif max_word < length_string and string == string[::-1]:
                    max_word = length_string
                    biggerSubstring = string 
                
            
            apontadorFim += 1
            if apontadorFim == length:
                apontadorFim = apontadorInicio = apontadorInicio + 1
                string = ""

            
            if apontadorInicio == length:
                break

        return biggerSubstring

            

            




""" 
       for letter in s:
            string_reversed = string[::-1]
            print(string_reversed)
            if string_reversed != string:
                string = string[1:]

            string += letter
            bigger =  max(len(string), max_word)
            if bigger > max_word:
                biggerSubstring = string
                max_word = bigger

        return biggerSubstring
"""
solution = Solution()
print(solution.longestPalindrome("abcba"))
