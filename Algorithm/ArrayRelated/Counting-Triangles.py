"""

[1, 1, 1, 2, 2]

1, 1, 1         O       1 + 1  >    1
1, 1, 2         X       1 + 1  <=   2
1, 1, 2         X
1, 1, 2         X
1, 1, 2         X
1, 2, 2         O       1 + 2   >   2
1, 1, 2         X
1, 1, 2         X
1, 2, 2         O       1 + 2   >   2
1, 2, 2         O       1 + 2   >   2

[1, 2, 2, 3]
1, 2, 2         O
1, 2, 3         X
1, 2, 3         X
2, 2, 3         O


"""

def counting_triangles(arr):
    arr.sort()
    len_arr = len(arr)
    counting = 0
    for i in range(len_arr - 2):
        for j in range(i+1, len_arr-1):
            for k in range(j+1, len_arr):
                if arr[i] + arr[j] > arr[k]:  # make triangle
                    counting += 1
                else:
                    break
    return counting


def counting_triangles_s(arr):
    arr.sort()
    len_arr = len(arr)
    counting = 0
    print(arr)
    for i in range(len_arr - 1, 1, -1):
        l = 0
        r = i - 1
        while l < r:
            print(l, r, i, arr[l], arr[r], arr[i], counting, (arr[l] + arr[r] > arr[i]))
            if arr[l] + arr[r] > arr[i]:    # make triangle
                counting += (r-l)
                r -= 1
            else:
                l += 1

    return counting

# test
input_arr = [1, 1, 1, 2, 2]

print(counting_triangles(input_arr))
print(counting_triangles_s(input_arr))
input_arr = [ 4, 6, 13, 16, 20, 3, 1, 12 ]
print(counting_triangles(input_arr))
print(counting_triangles_s(input_arr))