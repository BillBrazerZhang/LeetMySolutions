class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i in range(len(nums)-2):
        	if nums[i] > 0:
        		break
        	if i > 0 and nums[i] == nums[i-1]:
        		continue
        	l, r = i+1, len(nums)-1
        	while l < r:
        		s = nums[i] + nums[l] + nums[r]
        		if s > 0:
        			r -= 1
        		elif s < 0:
        			l += 1
        		else:
        			res.append([nums[i],nums[l],nums[r]])
        			while nums[l+1] == nums[l]:
        				l += 1
        			while nums[r-1] == nums[r]:
        				r -= 1
        			l += 1
        			r -= 1
        return res

a = Solution()
out = a.threeSum([-1,-2,0,4,2,1,-1])
print(out)


