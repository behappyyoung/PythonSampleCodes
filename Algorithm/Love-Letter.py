__author__ = 'young'
'''
James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows two rules:

He can reduce the value of a letter, e.g. he can change d to c, but he cannot change c to d.
In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until the letter becomes a. Once a letter has been changed to a, it can no longer be changed.
Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.
'''

import math

T = int(raw_input())
myinput =[]
for num in range(0, T):
    myinput.append(raw_input())



for i in myinput:
    tempArray =[]
    for c in i:
        tempArray.append(ord(c))

    num = 0
    step =0
    length = len(tempArray)


    while num < math.ceil(length/2):
        if tempArray[num]>=tempArray[num+1]:
           tempArray[num] = tempArray[num] -1
           step = step + 1
        else:
           if tempArray[num]==tempArray[num+1]-1:
              num = num + 1
           else:
              tempArray[num+1] = tempArray[num+1] -1
              step = step + 1

    num = length-1
    while num >= math.ceil(length/2) + 1:
        if tempArray[length-1] > tempArray[0]:
            tempArray[length-1] = tempArray[length-1]-1
            step = step + 1
        else:
            if tempArray[num-1]<=tempArray[num]:
                print 'input error'
            elif tempArray[num-1]-1 ==tempArray[num]:
                num = num - 1
            else:
                tempArray[num-1] = tempArray[num-1]-1
                step = step +1


    print step
