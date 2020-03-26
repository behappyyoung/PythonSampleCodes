"""

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


"""

def letterCombinations(A):
    phone = {
        '0': '0',
        '1': '1',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def makeCombinations(sl1, sl2):
        new_arr = []
        for i in range(len(sl1)):
            for j in range(len(sl2)):
                new_arr.append(sl1[i] + sl2[j])
        return new_arr

    al = list(str(A))
    r_arr = list(phone.get(al[0]))
    for i in range(1, len(al)):
        r_arr = makeCombinations(r_arr, list(phone.get(al[i])))

    return sorted(r_arr)

print(letterCombinations(1))
print(letterCombinations(23))
print(letterCombinations(134))
