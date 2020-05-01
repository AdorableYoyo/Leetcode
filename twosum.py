class Solution(object):
    def twoSum(self, nums,target):

        d = {}
        for i, j in enumerate(nums):
            if d.get(j) == None:
                d[target - j] = i
            else:
                return (d.get(j),i)