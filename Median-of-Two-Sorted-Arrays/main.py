import decimal

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        array = nums1 + nums2
        array.sort()
        decimal.getcontext().prec = 5
        print(decimal.Decimal(self.median(array)))
        
        

        
    def median(self, array):
        length = len(array)
        if length % 2 != 0:
            return array[length // 2]

        else:
            position = (length // 2) - 1
            return (array[position] + array[position + 1]) / 2
        


solution = Solution()
print(solution.findMedianSortedArrays([1,3], [2, 4]))


        