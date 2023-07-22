class Solution:
    def reverse(self, x: int) -> int:
        number_bigger_negative = -2 ** 31
        number_bigger_positive = (2 ** 31) - 1
        if x < number_bigger_negative or x > number_bigger_positive:
            return 0

        else:
            string = str(x)
            reverse = None
            if x < 0:
                temp = string[1:]
                reverse = "-" + temp[::-1]

            else:
                reverse = string[::-1]

            reverse = int(reverse)

            if reverse < number_bigger_negative or reverse > number_bigger_positive:
                return 0

            else:
                return reverse


reverse = Solution()
print(reverse.reverse(123))
