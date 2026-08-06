class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=Counter(nums)
        sorted_a = sorted(a, key=a.get, reverse=True)
        return sorted_a[:k]