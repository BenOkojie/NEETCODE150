 def hasDuplicate(self, nums: List[int]) -> bool:

        cur = 0
        tbl= set()
        print(tbl)
        while cur < len(nums):
            
            if nums[cur] in tbl:
                return True
            else:
                tbl.add(nums[cur])
            cur+=1
        return False
