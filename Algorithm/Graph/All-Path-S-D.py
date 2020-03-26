"""
Example:
Input: [[1,2], [3], [3], []]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

"""
def allPathsSourceTarget(graph):
    """
    :type graph: List[List[int]]
    :rtype: List[List[int]]
    """
    N = len(graph)

    def walk(node):
        if node == N - 1: return [[N - 1]]
        ans = []
        for np in graph[node]:
            for path in walk(np):
                ans.append([node] + path)
            # print(np, ans)
        return ans

    return walk(0)

print(allPathsSourceTarget([[1,2],[3,4],[4],[],[5], [6], []]))