#link : https://leetcode.com/problems/find-the-duplicate-number/

# 1. brute force: nested loops O(n^2)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numsize=len(nums)
        for i in range(0,numsize):
            for j in range(i+1, numsize):
                if nums[i]==nums[j]: return nums[i]


# 2. extra space and using sort func:
#list.sort() -> time complexity nlog(n) 
#total time =nlog(n) + O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ndup=nums
        ndup.sort();
        for i in range(0, len(nums)):
            j=i+1
            if ndup[i]==ndup[j]: return ndup[i]

#using extra space but time complexity o(n):
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N=len(nums)
        seen = [0] * (N)
        for i in nums:
            if seen[i]:
                return i
            seen[i]=1




