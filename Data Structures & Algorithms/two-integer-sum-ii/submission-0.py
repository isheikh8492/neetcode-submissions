class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number1 = None
        number2 = None
        index1 = None
        index2 = None

        for i in range(len(numbers)):
            number1 = numbers[i]
            if target - number1 in numbers:
                number2 = target - number1
                index1 = i
                break

        index2 = numbers.index(number2)

        return [index1+1, index2 + 1]
                
        