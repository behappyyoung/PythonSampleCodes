"""
Subset
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
S = [1,2,3]
[
  [],
-  [1],
-  [1, 2],
-  [1, 2, 3],
-  [1, 3],
  [2],
  [2, 3],
  [3],
]

[
  [],
  [1],
  [1, 2],
-  [1, 2, 3],
-  [1, 3],
  [2],
-  [2, 3],
-  [3],
]

subsets => print wrong order

"""



def subsets(arr):
    if len(arr) == 0:
        return [[]]
    arr.sort()
    subset_r = arr[-1]
    subset_sub = subsets(arr[:-1])
    new_subsets = [(ss+[subset_r]) for ss in subset_sub]

    new_subsets.sort()
    return  subset_sub + new_subsets


def subsets_s(arr):
    if len(arr) == 0:
        return [[]]
    arr.sort()
    subset_f = arr[0]
    subset_sub = subsets(arr[1:])

    new_subsets = [([subset_f] + ss) for ss in subset_sub]

    new_subsets.sort()
    print(subset_sub, new_subsets)

    new_subsets = new_subsets + subset_sub
    new_subsets.sort()
    return  new_subsets
# print(subsets([15, 2, 3]))
print(subsets_s([15, 2, 3]))
# print(subsets([12, 13]))
# print(subsets([ 15, 20, 12, 19, 4 ]))