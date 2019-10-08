
arr = []
for arr_i in range(6):
    arr_temp = map(int,input().strip().split(' '))
    arr.append(arr_temp)


maxsum = -63
for i in range(4):
    for j in range(4):
        sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        if sum > maxsum:
            maxsum = sum

print(maxsum)