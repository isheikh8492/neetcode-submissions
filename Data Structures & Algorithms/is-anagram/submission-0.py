class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.calculateDictionary(s) == self.calculateDictionary(t)

    def calculateDictionary(self, string: str) -> bool:
        dictionary = dict()
        for ch in string:
            if ch not in dictionary:
                dictionary.update({ch: 1})
            else:
                dictionary.update({ch: dictionary[ch] + 1})

        return dictionary
            
        