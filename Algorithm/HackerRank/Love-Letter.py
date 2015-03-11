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


def setFirstSmallest(intArray, smallnumber):
    stepcount =0
    while intArray[0] == smallnumber:
          intArray[0] = intArray[0]-1
          stepcount = stepcount +1
    return stepcount


def makePalindrome(intArray):
    stepcount = 0
    num = 0
    length = len(intArray)

    while num < math.ceil(length/2.0)-1:
##                print intArray
##            if intArray[0] > intArray[num]:                     ## if any number smaller than first one
  ##              stepcount = stepcount + setFirstSmallest(intArray, intArray[num])
    ##            stepcount = stepcount + makePalindrome(intArray)
      ##      else:
                if intArray[num]>intArray[num+1]:                  ## current > next
                   intArray[num] = intArray[num] -1
                   stepcount = stepcount + 1
                elif intArray[num]==intArray[num+1]:                  ## current == next
                    if intArray[num] == 97:
                        if num == 0:
                           num = num + 1
                        elif intArray[num-1] == 97:
                           num = num + 1
                        elif intArray[num] < intArray[num-1]:
                           intArray[num-1] = intArray[num-1] -1
                           num = num -1
                    else:
                        intArray[num] = intArray[num] -1
                        stepcount = stepcount + 1
                        if num == 0:
                           num = num + 1
                        elif intArray[num] <= intArray[num-1]:
                           num = num -1
                        else:
                           num = num + 1
                else:                                               ## current < next
                   if intArray[num]==intArray[num+1]-1:             ## current == next -1
                      num = num +1
                   else:
                      intArray[num+1] = intArray[num+1] -1
                      stepcount = stepcount + 1
    num = length-1
    while num > math.floor(length/2.0) :
##            print intArray
            if intArray[length-1] > intArray[0]:               ## last > first
                intArray[length-1] = intArray[length-1]-1
                stepcount = stepcount + 1
                num = length-1

            else:                                               ## first == last
                if intArray[num-1] < intArray[num]:              ## before < current
                    if intArray[num] == 97:
                        print 'input error'
                        return stepcount
                    else:
                        intArray[num] = intArray[num] -1
                        num = num + 1
                elif intArray[num-1] == intArray[num]:              ## before == current
                    if intArray[num] == 97:
                        if num == length-1:
                           num = num - 1
                        elif intArray[num+1] == 97:
                           num = num - 1
                        elif intArray[num] < intArray[num+1]:
                           intArray[num+1] = intArray[num+1] -1
                           num = num +1
                    else:
                        intArray[num] = intArray[num] -1
                        stepcount = stepcount + 1
                        if num == length-1:
                           num = num - 1
                        elif intArray[num] <= intArray[num+1]:
                           num = num + 1
                        else:
                           num = num - 1


                elif intArray[num-1]-1 ==intArray[num]:
                    num = num - 1
                else:
                    intArray[num-1] = intArray[num-1]-1
                    stepcount = stepcount +1


    if length % 2 ==0:          ## even number of array   #### do agin
       middle = length/2-1
       if intArray[middle]== intArray[middle+1]:
            return stepcount
       elif intArray[middle] > intArray[middle+1]:
           while intArray[middle] > intArray[middle+1]:
                intArray[middle] =  intArray[middle] -1
                stepcount = stepcount + 1
           stepcount = stepcount + makePalindrome(intArray)
           return stepcount
       else:
           while intArray[middle] < intArray[middle+1]:
               intArray[middle+1] =  intArray[middle+1] -1
               stepcount = stepcount + 1
           stepcount = stepcount + makePalindrome(intArray)
           return stepcount
    else:
        middle = length/2-1
        if intArray[middle] == intArray[middle-1]+1:
           if intArray[length/2] == intArray[length/2+1]+1:
                return stepcount
           elif intArray[middle] > intArray[middle+1]+1:
                while intArray[middle] > intArray[middle+1]+1:
                    intArray[middle] =  intArray[middle]-1
                    stepcount = stepcount + 1
                stepcount = stepcount + makePalindrome(intArray)
                return stepcount
           else:
                while intArray[middle] < intArray[middle+1]+1:
                    intArray[middle-1] =  intArray[middle+1] -1
                    stepcount = stepcount + 1
                stepcount = stepcount + makePalindrome(intArray)
                return stepcount

        elif intArray[middle] > intArray[middle-1]+1:
            while intArray[middle] > intArray[middle-1]+1:
                intArray[middle] =  intArray[middle] -1
                stepcount = stepcount + 1
            stepcount = stepcount + makePalindrome(intArray)
            return stepcount
        else:
           while intArray[middle] < intArray[middle-1]+1:
                intArray[middle-1] =  intArray[middle-1] -1
                stepcount = stepcount + 1
           stepcount = stepcount + makePalindrome(intArray)
           return stepcount

for i in myinput:
    tempArray =[]
    for c in i:
        tempArray.append(ord(c))

    print makePalindrome(tempArray)

