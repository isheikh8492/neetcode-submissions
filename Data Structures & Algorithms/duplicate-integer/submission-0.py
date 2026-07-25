class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        present_already = set()
        for num in nums:
            if num not in present_already:
                present_already.add(num)
            else:
                return True
        return False
         