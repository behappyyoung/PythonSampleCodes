__author__ = 'young'


T = int(raw_input())
myinput =[]
for num in range(0, T):
    myinput.append(raw_input())


######### too long for big range ==> killed
# def getSquareCount(first, last):
#     global caltime
#     print first, last
#     count = 0
#     for i in range(1, last/2):
#         caltime = caltime + 1
#         squareNumber = i*i
#         if squareNumber >= first and squareNumber <= last:
#             count = count + 1
#         elif squareNumber > last:
#             break
#
#     print count

def getSquareCount(first, last):
    count = 0
    mins = last/2
    i = 1
    while i <= mins:
        squareNumber = i*i
        if squareNumber >= first and squareNumber <= last:
            count = count + 1
            mins = last / i
        elif squareNumber > last:
            break
        i = i + 1

    print count


for lines in myinput:
    intArray = map(int, lines.split( ))
    getSquareCount(intArray[0], intArray[1])







