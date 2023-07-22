class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        tamanho = 0
        itens = []
        for i in range(len(numbers)):
            tamanho += 1
            if numbers[i] not in itens:
                itens.append(numbers[i])
                if numbers[i] == target:
                    try:
                        return [i + 1, numbers[i + 1:].index(0) + tamanho + 1]

                    except ValueError:
                        continue

                result = 0

                if numbers[i] >= 0 and target <= 0:
                    result = - (numbers[i] + (-target))


                elif numbers[i] < 0 and target < 0:
                    result = target - numbers[i]

                else:
                    result = abs(numbers[i] - target)

                try:
                    index = numbers[i + 1:].index(result)
                    return [i + 1, index + tamanho + 1]

                except ValueError:
                    pass

solution = Solution()
print(solution.twoSum([-1,0], -1))

