class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1 = [1]*len(nums)
        left = 1
        right = 1
        for i in range(len(nums)):
            nums1[i] = left
            left *= nums[i]


        for i in range(len(nums)-1, -1, -1):
            nums1[i] *= right
            right *= nums[i]


        return nums1