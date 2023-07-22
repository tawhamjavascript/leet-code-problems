class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

            elif nums[i] > target:
                return i

        return len(nums)

solution = Solution()
print(solution.searchInsert([1, 5, 6], 8))