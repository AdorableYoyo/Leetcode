class Solution(object):
    def isAnagram( self, s, t):
        if  len(s)==len(t):
            for i in t:
                if t.count(i)!= s.count(i):
                    return False
            return True
        return False
