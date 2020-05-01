

class Solution(object):
    def removeDuplicates(self , Y):
        if not Y:
            return 0

        long = 0
        for i in range(1, len(Y)):
            if Y[i] != Y[long]:
                long += 1
                Y[long] = Y[i]
        return (long + 1)

list = [1,1,1,1,2,3,3,5,5]

print(Solution.removeDuplicates(list, list))