class Solution:
    def searchRange(self, nums: 'List[int]', target: int) -> 'List[int]':
        lista = self.search(nums, target, len(nums))
        length = len(lista)
        if length == 0:
            return [-1, -1]

        elif length == 1:
            return lista + [lista[0]]

        else:
            return [min(lista), max(lista)]

    def search(self, nums: list, target: int, length, array=[]) -> list[int]:
        if len(nums) <= 0:
            return array

        try:
            i = nums.index(target)
            return self.search(nums[i+1:], target, length, array + [i + (length - len(nums))])

        except ValueError:
            return array


solution = Solution()
array = [[5,7,7,8,8,10], [5,7,7,8,8,10], []]
target = [8, 6, 0]
for i in range(len(array)):
    print(solution.searchRange(array[i], target[i]))








