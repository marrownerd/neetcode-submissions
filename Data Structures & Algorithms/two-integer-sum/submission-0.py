class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = {}
        for i,n in enumerate(nums):
            number = target - nums[i]
            if number in nums1:
                return [nums1[number], i]
            nums1[n]=i