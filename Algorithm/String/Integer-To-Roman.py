"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Input 1:
    A = 5
Output 1:
    "V"

Input 2:
    A = 14
Output 2:
    "XIV"


"""
def make_roman(int, current, middle, prev):
    return_str = ''
    if int == 9:
        return_str += (current + prev)
    elif 5 <= int <= 8:
        return_str += middle
        for i in range(6, int+1):
            return_str += current
    elif int == 4:
        return_str += (current + middle)
    else:
        for i in range(1, int+1):
            return_str += current
    return return_str

def integer_to_roman(int_val):
    roman_str = ''
    int_thousand = int(int_val / 1000)
    int_hundred = int ((int_val - int_thousand*1000) / 100)
    int_ten = int((int_val - int_thousand*1000 - int_hundred*100) / 10)
    int_one = int(int_val - int_thousand*1000 - int_hundred*100 - int_ten*10)

    for i in range(1, int_thousand+1):
        roman_str += 'M'

    roman_str += make_roman(int_hundred, 'C', 'D', 'M')
    roman_str += make_roman(int_ten, 'X', 'L', 'C')
    roman_str += make_roman(int_one, 'I', 'V', 'X')

    return roman_str

print(integer_to_roman(4))
print(integer_to_roman(1000))
print(integer_to_roman(2421))
print(integer_to_roman(3287))