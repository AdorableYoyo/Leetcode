class Solution(object):
    def containsDuplicate(self,a):
        return len(set(a))<len(a)