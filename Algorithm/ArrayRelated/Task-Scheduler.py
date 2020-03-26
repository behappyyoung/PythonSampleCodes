"""
task scheduler
[2,3,1,1,3,2,2,1] N=2 ( minimum space between same number)
=>
[2,3,1,0,0,1,3,2,0,0,2,1]

"""

def task_s(arr, n):
    if not arr or n == 0:
        return arr
    r_arr = []
    num_dict = {}
    for i in range(len(arr)):
        if arr[i] in num_dict:
            pre_l = num_dict[arr[i]]
            if i - pre_l < n:
                for j in range(n-(i-pre_l)):
                    r_arr.append(0)
            r_arr.append(arr[i])
            num_dict[arr[i]] = i
        else:
            r_arr.append(arr[i])
            num_dict[arr[i]] = i
    return r_arr

s = [2,3,1,1,3,2,2,1]

print(task_s(s, 2))