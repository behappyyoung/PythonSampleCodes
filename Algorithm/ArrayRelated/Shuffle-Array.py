"""

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

"""

import random

class Solution:

    def __init__(self, nums):
        self.original = list(nums)
        self.arr = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.arr = list(self.original)
        return self.arr

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.arr)):
            ri = random.randrange(len(self.arr))
            self.arr[i], self.arr[ri] = self.arr[ri], self.arr[i]
        return self.arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

obj = Solution([1,2,3, 4, 5, 6, 7])
print(obj.original)
print(obj.arr)

print(obj.shuffle())
print(obj.original)
print(obj.arr)

print(obj.reset())
