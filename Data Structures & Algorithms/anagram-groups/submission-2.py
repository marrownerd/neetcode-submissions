from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        numbers =  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97, 101]

        h_map = defaultdict(list)

        for s in strs:
            wordhash = 1
            for c in s:
                h_num = numbers[ord(c) - ord('a')]
                wordhash *= h_num
            
            h_map[wordhash].append(s)
        return list(h_map.values())
    


