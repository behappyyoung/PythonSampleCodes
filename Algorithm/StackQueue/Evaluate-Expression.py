"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Input 1:
    A =   ["2", "1", "+", "3", "*"]
Output 1:
    9
Explaination 1:
    starting from backside:
    *: ( )*( )
    3: ()*(3)
    +: ( () + () )*(3)
    1: ( () + (1) )*(3)
    2: ( (2) + (1) )*(3)
    ((2)+(1))*(3) = 9

Input 2:
    A = ["4", "13", "5", "/", "+"]
Output 2:
    6
Explaination 2:
    +: ()+()
    /: ()+(() / ())
    5: ()+(() / (5))
    1: ()+((13) / (5))
    4: (4)+((13) / (5))
    (4)+((13) / (5)) = 6


"""
def cal_ext(op, first_elem, second_elem):
    print('%s %s %s'% (second_elem, op, first_elem))
    first_int = int(first_elem)
    second_int = int(second_elem)
    if op == '/':
        result = second_int // first_int
    elif op == '*':
        result = second_int * first_int
    elif op == '+':
        result = second_int + first_int
    elif op == '-':
        result = second_int - first_int
    else:
        return 0
    print(op, first_elem, second_elem, result)
    return result

def evaluate_expression(arr):
    stack = []
    result = 0
    for i in range(len(arr)):
        if arr[i].lstrip('-+').isalnum():
            stack.append(arr[i])
        else:
            if len(stack) >= 2:
                first_elem  = stack.pop()
                second_elem = stack.pop()
                result = cal_ext(arr[i], first_elem, second_elem)
                stack.append(result)
        print(stack)
    if len(stack) > 0:
        if len(stack) >= 2:
            first_elem = stack.pop()
            second_elem = stack.pop()
            result = cal_ext(arr[i], first_elem, second_elem)
        else:
            result = stack.pop()
    return result
# test
input_arr =   ["2", "1", "+", "3", "*"]
# print(evaluate_expression(input_arr))
input_arr = ["4", "13", "5", "/", "+"]
# print(evaluate_expression(input_arr))
input_arr = [ "2", "3", "+", "4", "5", "+", "+", "6", "7", "+", "*", "2", "*" ] # 364
print(evaluate_expression(input_arr))