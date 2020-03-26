"""
For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

"""


def reverseInParentheses(inputString):
    l = inputString.rfind('(')
    r = inputString.find(')', l)
    while l != -1 and r != -1:
        inputString = inputString[:l] + inputString[l+1:r][::-1] + inputString[r+1:]
        l = inputString.rfind('(')
        r = inputString.find(')', l)

    return inputString


def reverseInParentheses_s(s):
    str = '"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"'
    # print(str)
    return eval(str)

# print(reverseInParentheses('(bar)'))
print(reverseInParentheses('foo(bar(baz))blim'))
print(reverseInParentheses_s('foo(bar(baz))blim'))
# print(reverseInParentheses('foo(bar)baz(blim)'))
print(reverseInParentheses('(d(abc)f)'))
print(reverseInParentheses_s('(d(abc)f)'))
# print(reverseInParentheses_s('((abc))'))
# print(reverseInParentheses('(())(())'))
# print(reverseInParentheses('(abc)(def)'))  # "cbafed"
# print(reverseInParentheses('aaa((babb))((baacbbb))aaa'))
print(reverseInParentheses('The ((quick (brown) (fox) jumps over the lazy) dog)'))
# print(reverseInParentheses_s('(quick (brown) (fox) jumps over the lazy)'))
print(reverseInParentheses_s('The ((quick (brown) (fox) jumps over the lazy) dog)'))
# "The ((quick (brown) (fox) jumps over the lazy) dog)"
# "The god quick nworb xof jumps over the lazy"

