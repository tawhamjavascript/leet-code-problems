class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)

        elif nums[0] > target:
            return 0

        try:
            return nums.index(target)

        except ValueError:
            index = self.search(nums, target, 0, len(nums) - 1)
            return index

    def search(self, nums, target, inicio, fim):
        if len(nums) == 0:
            return - 1

        if nums[0] > target:
            return inicio

        elif nums[-1] < target:
            return fim

        return self.search(nums[1:-1], target, inicio + 1, fim - 1)










solution = Solution()
print(solution.searchInsert([1, 3], 2))


