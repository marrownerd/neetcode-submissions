class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        
        nums.sort()
        curr = nums[0]
        strk = 0
        maximum = 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                strk = 0
            while i < len(nums) and nums[i]==curr:
                i +=1
            strk += 1
            curr += 1
            maximum = max(strk, maximum)

        return maximum


            

