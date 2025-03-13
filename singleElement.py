def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)-1
        if n+1 == 1:
            return nums[0]
        midpoint = n/2
        start = 0
        end = n
        print(nums)
        while end-start > 2:
            if nums[midpoint] != nums[midpoint-1] and nums[midpoint] != nums[midpoint+1] :
                return nums[midpoint]
            isEven = ((end-midpoint)%2) != 0
            print(nums[start:end+1])
            if isEven is True:
                if nums[midpoint] != nums[midpoint-1]:
                    end = midpoint-1
                else:
                    start=midpoint+1
            else:
                if nums[midpoint] != nums[midpoint-1]:
                    start = midpoint
                else:
                    end=midpoint
            midpoint = (end+start)/2
        if nums[midpoint] != nums[midpoint-1] and nums[midpoint] != nums[midpoint+1] :
            return nums[midpoint]
        else:
            if nums[midpoint] != nums[midpoint+1]:
                return nums[midpoint+1]
            else:
                return nums[midpoint-1]

