"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right.
You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles

"""
def avoidObstacles(inputArray):
    canD = False
    inputArray.sort()
    for i in range(2, 1001):
        for j in range(len(inputArray)):
            if inputArray[j] % i == 0:
                canD = True
                break
        if not canD:
            return i
        canD = False


def avoidObstacles_s(arr):
    canD = False
    arr.sort()
    m = max(arr)
    for i in range(2, m+2):
        for j in range(len(arr)):
            if arr[j] % i == 0:
                canD = True
                break
        if not canD:
            return i
        canD = False


#
testArray = [5, 3, 6, 7, 9]
print(avoidObstacles(testArray))
print(avoidObstacles_s(testArray))

testArray = [5, 3, 6, 7, 9, 999, 1000]
print(avoidObstacles(testArray))
print(avoidObstacles_s(testArray))

testArray = [1, 2, 4, 7, 10]
print(avoidObstacles(testArray))
print(avoidObstacles_s(testArray))