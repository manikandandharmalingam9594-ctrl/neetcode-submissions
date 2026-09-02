class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max=[]
        a=Counter(nums)
        return [i for i,j in a.most_common(k)]

        