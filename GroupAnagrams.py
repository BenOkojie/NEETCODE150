 def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # ltr = [None]*26
        anagrams={}
        ang = []
        # print(ltr)
        for i in strs:
            count = 0
            for j in i:
                count+= hash(j)
            if count not in anagrams:
                index = len(ang)
                anagrams[count] = index
                ang.append([i])
            else:
                ang[anagrams[count]].append(i)
        return ang
