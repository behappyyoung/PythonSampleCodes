# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    
    answer = 0
    # write code to compute answer
    print A, B, C1
    buy = int(A / B)
    wrapper = buy
    extra = int(wrapper / C1)
    wrapper = buy + extra  - (extra * C1)   ## total wrapper remaining
    extra = int (wrapper / C1) + extra
    print buy+extra
##    print answer

