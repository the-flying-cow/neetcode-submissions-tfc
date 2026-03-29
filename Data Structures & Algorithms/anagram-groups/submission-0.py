class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= []
        hash= defaultdict(list)
    # assign an empty list to a missing key value
    # later if we have a value for that key, we append it to list
        for s in strs:
            sorted_s= "".join(sorted(s))
            hash[sorted_s].append(s)
    # sorted returns a new string, leaving the original unchanged
        for values in hash.values():
            res.append(values)
        return res