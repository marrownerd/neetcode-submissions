class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        biggest = 0

        for n in num_set:
            if n-1 not in num_set:
                length = 0
                while (n+length) in num_set:
                    length += 1
                biggest = max(biggest, length)

        return biggest


        



            

