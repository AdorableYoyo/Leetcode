class Solution(object):
    def isValid( self, s):
        d = {'}':'{',
        ')':'(',
        ']':'['}
        open = d.values()
        l = []
        for i in s:
            if i in open:
                l.append(i)
            else:
                if len(l)>0 and l[-1] == d.get(i):
                    l.pop()
                else:
                    return False
        return len(l)==0