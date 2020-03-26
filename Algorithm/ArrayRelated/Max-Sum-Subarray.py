"""
https://www.interviewbit.com/problems/max-sum-contiguous-subarray/
Input 1:
    A = [1, 2, 3, 4, -10]

Output 1:
    10

Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4];

Output 2:
    6

Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.

"""
def max_sum_subarray(arr):
    best_max = current_sum = mid_sum = arr[0]
    start = end = current_start = mid_start = 0
    for i in range(1, len(arr)):
        if arr[i] > 0:      # value is positive
            current_sum += arr[i]
            if arr[i] > current_sum:
                current_sum = arr[i]
                current_start = i

            if mid_sum == 0:
                mid_start = i
            mid_sum += arr[i]

            if mid_sum > current_sum:
                current_sum = mid_sum
                current_start = mid_start
                if mid_sum > best_max:
                    best_max = current_sum
                    start = mid_start
                    end = i

            elif current_sum > best_max:
                best_max = current_sum
                start = current_start
                end = i

        elif arr[i] == 0:       # value is 0
            if 0 > best_max:
                current_sum = best_max = 0
                start = end = i
            else:
                end = i
        else:                   # value is minus
            current_sum += arr[i]
            if arr[i] > current_sum:
                current_sum = arr[i]
                current_start = i
            if current_sum > best_max:
                best_max = current_sum
                start = current_start
                end = i
            mid_sum = 0

    print(arr, ':', start, end, arr[start:end+1], best_max)

def max_r(arr, s, e):
    if len(arr) ==1:
        return arr[0]

def max_sum_subarray_r(arr):
    if len(arr) ==1:
        return arr[0]


def max_sum_subarray_dc(arr, s, e):
    if not arr:
        return ''
    s = 0 if not s else s
    e = len(arr)-1 if not e else e
    if e == 0:
        return arr[0]
    m = e // 2
    max_sub = max(max_sum_subarray_dc(arr, s, m), max_sum_subarray_dc(arr, m+1, e))
    return max_sub

def max_sum(arr):
    max_sum = -2**32
    max_sofar = max_sum
    for i in range(len(arr)):
        max_sofar = max(arr[i], max_sofar+arr[i])
        if max_sofar > max_sum:
            max_sum = max_sofar
    return max_sum

# test
test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum_subarray(test_array)
print(max_sum(test_array))
test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 2, 2]
max_sum_subarray(test_array)
print(max_sum(test_array))
test_array = [ 1, 2, 5, 0, -70, 2, 50 ]
max_sum_subarray(test_array)
print(max_sum(test_array))
test_array = [ -1, -1, -1 ]
max_sum_subarray(test_array)
print(max_sum(test_array))
test_array = [ -1, 0, 0, -1, -1, -1 ]
max_sum_subarray(test_array)
print(max_sum(test_array))
# test_array = [ -120, -202, -293, -60, -261, -67, 10, 82, -334, -393, -428, -182, -138, -167, -465, -347, -39, -51, -61, -491, -216, -36, -281, -361, -271, -368, -122, -114, -53, -488, -327, -182, -221, -381, -431, -161, -59, -494, -406, -298, -268, -425, -88, -320, -371, -5, 36, 89, -194, -140, -278, -65, -38, -144, -407, -235, -426, -219, 62, -299, 1, -454, -247, -146, 24, 2, -59, -389, -77, -19, -311, 18, -442, -186, -334, 41, -84, 21, -100, 65, -491, 94, -346, -412, -371, 89, -56, -365, -249, -454, -226, -473, 91, -412, -30, -248, -36, -95, -395, -74, -432, 47, -259, -474, -409, -429, -215, -102, -63, 80, 65, 63, -452, -462, -449, 87, -319, -156, -82, 30, -102, 68, -472, -463, -212, -267, -302, -471, -245, -165, 43, -288, -379, -243, 35, -288, 62, 23, -444, -91, -24, -110, -28, -305, -81, -169, -348, -184, 79, -262, 13, -459, -345, 70, -24, -343, -308, -123, -310, -239, 83, -127, -482, -179, -11, -60, 35, -107, -389, -427, -210, -238, -184, 90, -211, -250, -147, -272, 43, -99, 87, -267, -270, -432, -272, -26, -327, -409, -353, -475, -210, -14, -145, -164, -300, -327, -138, -408, -421, -26, -375, -263, 7, -201, -22, -402, -241, 67, -334, -452, -367, -284, -95, -122, -444, -456, -152, 25, 21, 61, -320, -87, 98, 16, -124, -299, -415, -273, -200, -146, -437, -457, 75, 84, -233, -54, -292, -319, -99, -28, -97, -435, -479, -255, -234, -447, -157, 82, -450, 86, -478, -58, 9, -500, -87, 29, -286, -378, -466, 88, -366, -425, -38, -134, -184, 32, -13, -263, -371, -246, 33, -41, -192, -14, -311, -478, -374, -186, -353, -334, -265, -169, -418, 63, 77, 77, -197, -211, -276, -190, -68, -184, -185, -235, -31, -465, -297, -277, -456, -181, -219, -329, 40, -341, -476, 28, -313, -78, -165, -310, -496, -450, -318, -483, -22, -84, 83, -185, -140, -62, -114, -141, -189, -395, -63, -359, 26, -318, 86, -449, -419, -2, 81, -326, -339, -56, -123, 10, -463, 41, -458, -409, -314, -125, -495, -256, -388, 75, 40, -37, -449, -485, -487, -376, -262, 57, -321, -364, -246, -330, -36, -473, -482, -94, -63, -414, -159, -200, -13, -405, -268, -455, -293, -298, -416, -222, -207, -473, -377, -167, 56, -488, -447, -206, -215, -176, 76, -304, -163, -28, -210, -18, -484, 45, 10, 79, -441, -197, -16, -145, -422, -124, 79, -464, -60, -214, -457, -400, -36, 47, 8, -151, -489, -327, 85, -297, -395, -258, -31, -56, -500, -61, -18, -474, -426, -162, -79, 25, -361, -88, -241, -225, -367, -440, -200, 38, -248, -429, -284, -23, 19, -220, -105, -81, -269, -488, -204, -28, -138, 39, -389, 40, -263, -297, -400, -158, -310, -270, -107, -336, -164, 36, 11, -192, -359, -136, -230, -410, -66, 67, -396, -146, -158, -264, -13, -15, -425, 58, -25, -241, 85, -82, -49, -150, -37, -493, -284, -107, 93, -183, -60, -261, -310, -380 ]
# test_array = [ -338, -30, -484, -171, -254, -89, 10, -471, 67, -420, -20, -445, -220, -122, 29, -437, -102, -145, -193, -75, -261, -456, -146, -122, -102, 51, -35, -125, -391, -251, -226, -359, -60, -190, -381, -417, 13, -165, -282, -117, -489, 14, -81, -366, -187, -35, -410, 9, -322, -211, -492, -132, -146, -69, 23, 83, 58, -500, 92, -51, -90, -255, -56, -483, -170, 68, 14, -19, 74, 34, -264, -294, -245, -38, -206, 45, -283, -124, -339, -361, -89, 4, -235, 66, -430, 12, -174, -272, -288, 2, -97, -427, -476, -325, -478, 20, -309, -78, -77, -362, -492, -118, -267, 48, -478, -450, -146, -487, -86, -147, -185, -249, -37, 26, -89, 39, -413, -64, -377, -326, -342, -191, -151, -89, -148, -454, -167, -419, -194, -288, -194, -141, -127, -471, -397, -396, -176, -3, 34, -98, -73, -339, -91, -127, -315, 89, -411, -23, -95, -22, -252, 43, 38, -140, -329, -176, 94, -81, -139, 66, -98, -110, -394, -451, -102, -250, -121, -361, -357, -395, -125, -148, -207, -208, 40, -352, 42, -69, 31, -161, -371, 39, -143, -113, -55, 1, -126, -248, -299, -397, -188, -353, 77, -150, -163, -406, -291, -363, -343, -6, -241, -279, -120, 1, -45, 92, -245, -253, -312, -379, -322, -410, -83, -491, -332, -174, 67, -404, -182, -226, -192, 27, -335, -83, -332, -270, -295, -184, 70, -218, -398, -149, -286, -402, -178, -55, -482, -436, -152, -81, -330, -6, 41, -427, -205, -430, -162, -7, 23, 60, -99, -437, 81 ]
# test_array = [ 1, 2, -5, 20, -10, 2, 50 ]
test_array = [ -160, -20 ]
max_sum_subarray(test_array)
print(max_sum(test_array))