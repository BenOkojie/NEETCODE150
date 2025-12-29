class Solution:
    def findMin(self, nums: List[int]) -> int:
        l= 0
        r = len(nums)-1
        mid = int((l+r)/2)
        while r-l>1:
            if nums[mid]<nums[l] and nums[mid]<nums[r]:
                if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                    return nums[mid]
                else:
                    if nums[mid-1] < nums[mid]:
                        r=mid-1
                        mid = int((r+l)/2)
                    else:
                        l=mid+1
                        mid = int((r+l)/2)
            else:
                if nums[l] < nums[r]:
                    r = mid 
                    mid = int((r+l)/2)
                else:
                    l = mid 
                    mid = int((r+l)/2)
        return min(nums[l],nums[r])
        
