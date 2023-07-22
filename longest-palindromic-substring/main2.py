"""class Solution:
    def longestPalindrome(self, s: str) -> str:
        dict = {}
        left = right = 0
        length = len(s) - 1
        max_length = -1
        max_substring = ""
        string = ""
        for i in range(len(s)):
            if max_length < 1:
                max_length = 1
                string = s[right]
                dict[string] = max_length

            else:



solution = Solution()
print(solution.longestPalindrome("abcba"))
"""