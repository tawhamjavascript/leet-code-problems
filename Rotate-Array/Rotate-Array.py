class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        for i in range(k):
            last = nums.pop()
            nums.insert(0, last)

        print(nums)

string = ""


solution = Solution()
solution.rotate([-1,-100,3,99], 2)

