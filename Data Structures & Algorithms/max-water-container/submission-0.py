class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0

        i = 0
        j = len(heights)-1
        while i<j:
            vol = min(heights[i],heights[j])*(j-i)
            volume = max(vol, volume)
            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1
        return volume

        

        volume 
        