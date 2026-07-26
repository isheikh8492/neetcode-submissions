class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = dict()

        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s not in table.keys():
                table[sorted_s] = [s]
            else:
                table[sorted_s] += [s]

        result = []
        for t in table.keys():
            result.append(table[t])
        return result