class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp not in res:
                res[temp] = [i]
            else:
                res[temp].append(i)
        return res.values()
