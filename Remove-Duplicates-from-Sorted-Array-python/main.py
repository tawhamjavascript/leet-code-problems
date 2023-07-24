class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for i in range(len(nums) - 2, -1, -1):    
            if (nums[i] == nums[i + 1]):
                nums.pop(i + 1)
                k += 1

        return k


teste = [1, 1, 2]
solution = Solution()
solution.removeDuplicates(teste)
print(teste)
