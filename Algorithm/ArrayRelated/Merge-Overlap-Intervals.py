"""
https://www.interviewbit.com/problems/merge-overlapping-intervals/

Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

"""
def merge_overlap_intervals(arr_list):
    return_list = []
    skip = False
    for i in range(len(arr_list)-1):
        if skip:
            if c_arr[1] > arr_list[i+1][0]:
                right_max = max(c_arr[1], arr_list[i+1][1])
                c_arr = [c_arr[0], right_max]
                skip = True
            else:
                skip = False
        else:
            if arr_list[i][1] > arr_list[i+1][0]:
                right_max = max(arr_list[i][1], arr_list[i + 1][1])
                c_arr = [arr_list[i][0], right_max]
                skip = True
            else:
                c_arr = arr_list[i]
                skip = False
        if not skip:
            return_list.append(c_arr)
    if skip:
        return_list.append(c_arr)
    else:
        return_list.append(arr_list[-1])
    return return_list

# test
test_list = [[1,3],[4,6],[5,17],[15,18]]
print(merge_overlap_intervals(test_list))
test_list = [(1,3),(2,6),(5,10),(15,18)]
print(merge_overlap_intervals(test_list))
test_list = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
print(merge_overlap_intervals(test_list))
test_list = [ (2, 10), (1, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
print(merge_overlap_intervals(test_list))