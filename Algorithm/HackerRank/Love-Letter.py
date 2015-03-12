__author__ = 'young'
'''
James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows two rules:

He can reduce the value of a letter, e.g. he can change d to c, but he cannot change c to d.
In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until the letter becomes a. Once a letter has been changed to a, it can no longer be changed.
Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.
'''
import socket

import math

T = int(raw_input())
myinput =[]
for num in range(0, T):
    myinput.append(raw_input())


def makePalindrome(intArray):
    stepcount = 0
    length = len(intArray)
    i = 0
    j = length -1

    while i <= math.ceil(length/2.0)-1:
        gonext = 'stay'
        if socket.gethostname()=='young-ubuntu-honda':
            print i, j, ' :' , stepcount, '  ', intArray
        if intArray[i] == intArray[j]:
            if i==j or j-i==1:
                gonext = 'next'

            elif intArray[i] == 97:                                 ## i, j value == 97
                if 1 >= intArray[i+1] - intArray[i]:
                    if 1 >= intArray[j-1] - intArray[j]:            ## both i+1, j-1  value  <=98
                        gonext = 'next'
                    else:
                        intArray[j-1] = intArray[j-1] -1
                        stepcount = stepcount + 1
                else:
                    if 1 >= intArray[j-1] - intArray[j]:
                        intArray[i+1] = intArray[i+1] -1
                        stepcount = stepcount + 1
                    else:
                        intArray[j-1] = intArray[j-1] -1
                        stepcount = stepcount + 1
            elif i!=0 and 1 > intArray[i]-intArray[i-1]:
                gonext = 'prev'
            elif 1 > intArray[i+1]-intArray[i]:
                intArray[i] = intArray[i] -1
                intArray[j] = intArray[j] -1
                stepcount = stepcount + 2
            elif 1 > intArray[j-1]-intArray[j]:
                intArray[i] = intArray[i] -1
                intArray[j] = intArray[j] -1
                stepcount = stepcount + 2
            elif 1 < intArray[i+1]-intArray[i]:
                intArray[i+1] = intArray[i+1] -1
                stepcount = stepcount + 1
            elif 1 < intArray[j-1]-intArray[j]:
                intArray[j-1] = intArray[j-1] -1
                stepcount = stepcount + 1
            else:
                gonext = 'next'

        elif intArray[i]<intArray[j]:
            intArray[j] = intArray[j] - 1
            stepcount = stepcount + 1
        else:
            intArray[i] = intArray[i] - 1
            stepcount = stepcount + 1

        if gonext == 'next':
            i = i + 1
            j = j - 1
        elif gonext == 'prev':
            i = i -1
            j = j + 1

    return stepcount

for i in myinput:
    intArray =[]
    for c in i:
        intArray.append(ord(c))

    print makePalindrome(intArray)

