class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        begin = 0
        end = len(s) - 1;
        while begin < end:
            if not s[begin].isalnum():
                begin += 1
                continue

            if not s[end].isalnum():
                end -= 1
                continue

            if s[begin] != s[end]:
                return False
            
            begin += 1
            end -= 1
            
        return True
    

solution = Solution()

print(solution.isPalindrome("0P"))