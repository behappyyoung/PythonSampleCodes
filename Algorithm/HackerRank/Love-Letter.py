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
        if i==j or j-i==1:
            break
	if i > 10:
		break
        gonext = 'stay'
<<<<<<< HEAD
##        print i, j, ' :' , stepcount, '  ', intArray
        if intArray[i] == intArray[j]:                               ## should be  [i] == [j] always
            idiff = int(intArray[i+1]-intArray[i])
            jdiff = int(intArray[j-1]-intArray[j])
	    print i, j, intArray[i], intArray[i+1], intArray[j-1], intArray[j], idiff, jdiff, stepcount
	    if idiff ==1 and jdiff ==1:
                gonext = 'next'

            elif 1 < idiff:
                intArray[i+1] = intArray[i+1] - ( idiff - 1 )
                stepcount = stepcount + ( idiff - 1 )
            elif 1 < jdiff:
                intArray[j-1] = intArray[j-1] - ( jdiff - 1)
                stepcount = stepcount +  ( jdiff - 1 )

	    elif 0 > idiff:
	            intArray[i] = intArray[i]+idiff
	            stepcount = stepcount -idiff

            elif 0 > jdiff:
	                intArray[j] = intArray[j] +jdiff
	                stepcount = stepcount  - jdiff

	    elif 0== idiff:
		    if i!=0 and intArray[i] >= 98 :
			intArray[i] = intArray[i]  -1
	                intArray[j] = intArray[j] -1
	                stepcount = stepcount  + 2
                    	gonext = 'prev'
		    else:
			gonext = 'next'	

            elif 0== jdiff:
		    if i!=0 and intArray[i] >= 98 :
			intArray[i] = intArray[i]  -1
	                intArray[j] = intArray[j] -1
	                stepcount = stepcount  + 2
                    	gonext = 'prev'
		    else:
			gonext = 'next'	
                
           
=======
        if (i !=0) and (  i==j or j-i==1) :
                break

        if intArray[i] == intArray[j]:                               ## should be  [i] == [j] always
            if intArray[i+1] != intArray[j-1]:
                if intArray[i+1]<intArray[j-1]:
                    diff = intArray[j-1]-intArray[i+1]
                    intArray[j-1] = intArray[j-1] - diff
                    stepcount = stepcount + diff
                else:
                    diff = intArray[i+1]-intArray[j-1]
                    intArray[i+1] = intArray[i+1] - diff
                    stepcount = stepcount + diff
            else:
                gonext = 'next'
>>>>>>> 42a57001c2336187c4b6f08870f341f7cc6cabaf

        elif intArray[i]<intArray[j]:
            diff = intArray[j]-intArray[i]
            intArray[j] = intArray[j] - diff
            stepcount = stepcount + diff
        else:
            diff = intArray[i]-intArray[j]
            intArray[i] = intArray[i] - diff
            stepcount = stepcount + diff

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
        intArray.append(int(ord(c)))

    print makePalindrome(intArray)

