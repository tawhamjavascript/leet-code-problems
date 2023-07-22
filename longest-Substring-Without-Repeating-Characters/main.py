class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        max_length = -1

        if len(s) == 0:
            return 0

        elif len(s) == 1:
            return 1

        for letter in s:
            if letter in string:
                string = string[string.index(letter) + 1: ]

            string += letter
            max_length = max(len(string), max_length)

        return max_length

        

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))



