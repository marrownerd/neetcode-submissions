class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i, m in enumerate(nums):
            if m > 0:
                break

            if i > 0 and m == nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l<r:
                if nums[r]+nums[l]+m>0:
                    r-=1
                elif nums[r]+nums[l]+m<0:
                    l+=1
                else:
                    result.append([m, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l< r:
                        l+=1
        return result






