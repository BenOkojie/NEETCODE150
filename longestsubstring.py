class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        subset=set()
        res = 0
        l=0
        r=1
        subset.add(s[l])
        while r<len(s):
            if s[r] in subset:
                res = max(res,len(subset))
                subset.remove(s[l])
                l+=1
            else:
                subset.add(s[r])
                r+=1
        res = max(res,len(subset))
        return res

        
