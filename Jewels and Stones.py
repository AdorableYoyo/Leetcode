
class Solution(object):
    def numJewelsInStones(self, J, S):
        return sum([i in J for i in S])
