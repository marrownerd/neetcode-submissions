class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        all = {}
        fr = [[] for i in range(len(nums)+1)]

        for num in nums:
            all[num] = 1 + all.get(num, 0)
        for num, cnt in all.items():
            fr[cnt].append(num)

        res = []
        for i in range(len(fr) - 1, 0, -1):
            for num in fr[i]:
                res.append(num)
                if len(res) == k:
                    return res