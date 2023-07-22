class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pass

    def search(self, numbers: list, target: int):
        if len(numbers) == 0:
            return - 1

        number = abs(numbers[0] - target)
        try:
            index = number.index(number)
            return []
