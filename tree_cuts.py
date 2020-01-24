import math

def countValleys(A=[]):
    if len(A) < 2:
        return 0,0

    tree = A.copy()
    tree.insert(0, math.inf)
    tree.append(math.inf)

    oddValleys = 0
    evenValleys = 0

    even = True
    for i in range(1, len(tree) - 1):

        if tree[i - 1] > tree[i] and tree[i] < tree[i + 1]:
            if (even):
                evenValleys += 1
            else:
                oddValleys += 1

        even = not even
    return evenValleys, oddValleys

def solution(A):
    n = len(A)
    if n < 2:
        return 0
    if n == 2:
        if A[0] != A[1]:
            return 0
        else:
            return 1
    
    evenValleys, oddValleys = countValleys(A)
    evenCuts = math.ceil(n/2.0) - evenValleys
    oddCuts = math.floor(n/2.0) - oddValleys

    return min([evenCuts, oddCuts])

# Algorithm
# O ( N )
# The optimal solution we are looking for has either:
#
# valleys in all even i:
# 
# \ / \ / \ /
#  1 9 2 8 3
#
# or valleys in all odd i:
#
# / \ / \ / \
#  9 1 8 2 3
#
# No other solution exists.
#
# Thus, we count the currently existing valleys
# and measure the distance to arrive in either of those
# options.
# 
# \0/1\2/
# Number of cuts for even-valleys solution:
# evenCuts = ceil(N/2) - evenValleys
#
# /0\1/2\
# Number of cuts for odd-valleys solution:
# oddCuts = floor(N/2) - oddValleys
# 