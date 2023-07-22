class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            index = nums.index(target)
            return index

        except:
            tamanho = len(nums) - 1
            index = abs(tamanho - target)
            if index > tamanho:
                return tamanho + 1
            else:
                while True:
                    if nums[index] > target:
                        return index

                    elif nums[index] < target:
                        index += 1


                    if index > tamanh