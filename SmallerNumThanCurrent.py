class Solution(object):

    def smallerNumbersThanCurrent(self, A):
        C = []
        for i in A:
            C.append(sum([i > j for j in A]))
        return C
