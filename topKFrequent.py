def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        topfreq = []
        tfreq = [[] for _ in range(len(nums)+1)]  
        print(tfreq)
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        print(freq)
        for ke, i in freq.items():
            # print(k)
            print("test")
            # print(i)
            tfreq[i].append(ke)
            print(tfreq)
        print(tfreq)
        i = len(tfreq) - 1
        while k>0:
            print(k)
            if not tfreq[i]:
                i-=1
            else:
                topfreq.append(tfreq[i].pop())
                k-=1
                
        return topfreq
            
