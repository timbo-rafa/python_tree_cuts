# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

increasing = True
decreasing = False

def countCuts(direction, A):
    # check if previous was cut
    # check if cut is gonna make tree 0

    previousWasCut = False
    cuts = 0
    prevH = A[0]
    for h in A[1:]:
        if h > prevH and direction == decreasing:
            previousWasCut = True
            cuts += 1
        if h < prevH and direction == increasing:
            previousWasCut = True
            cuts += 1
        prevH = h
        direction = not direction
    return cuts

def solution(A):
    # write your code in Python 3.6
    if len(A) < 3:
        return 0

    startIncreasingCuts = countCuts(increasing, A)
    startDecreasingCuts = countCuts(decreasing, A)
    
    return min( startDecreasingCuts, startIncreasingCuts)