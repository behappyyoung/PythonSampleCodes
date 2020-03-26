"""
reverse array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3

r = [3, 2, 1, 6, 5, 4, 9, 8, 7]
"""

def reverse_k(arr, k):
    print(arr)
    i = 0
    n = len(arr)
    while i <n:
        left = i
        right = min(i+k-1, n-1)

        while left < right:
            print(left, right)
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        i +=k

#test
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

reverse_k(arr, 3)
print(arr)

