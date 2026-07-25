from collections import OrderedDict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = OrderedDict()

        for num in nums:
            frequency.update({num: 1 if num not in frequency else frequency[num] + 1})

        result = []
        for k, v in sorted(frequency.items(), key=lambda c: -c[1])[:k]:
            result.append(k)

        return result

        