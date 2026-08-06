class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for word in strs:
            key=tuple(sorted(Counter(word).items()))
            mp[key].append(word)
        return list(mp.values())