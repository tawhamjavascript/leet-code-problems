class Solution:
    def firstBadVersion(self, n: int) -> int:
        array = [i + 1 for i in range(n)]
        return self.search(array)


    def search(self, array):
        if len(array) == 0:
            return - 1

        mid = len(array) // 2
        temp = array[mid]

        if self.isBadVersion(temp):
            for i in range(mid - 1, -1, -1):
                if self.isBadVersion(array[i]):
                    temp = array[i]

                else: return temp

            return temp

        else:
            return self.search(array[mid + 1: ])

    def isBadVersion(self, n):
        if n >= 1: return True
        else: return False


solution = Solution()
print(solution.firstBadVersion(1))








