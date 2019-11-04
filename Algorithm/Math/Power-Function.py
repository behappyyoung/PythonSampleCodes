"""

Implement pow(x, n)


"""
from datetime import datetime

def power_function(x, y):
    if y == 0:
        return 1
    else:
        for i in range(y):
            x *= x
        return x


def power_function_s(x, y):
    if y == 0:
        return 1
    elif int(y % 2) == 0:
        return power_function_s(x, int(y / 2)) * power_function_s(x, int(y / 2))
    else:
        return x * power_function_s(x, int(y / 2)) * power_function_s(x, int(y / 2))


def power_function_s_s(x, y):
    if y == 0:
        return 1
    temp = power_function_s_s(x, y / 2)
    if y % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp


print(power_function_s(-1, 2))
print(power_function_s(-1, 3))
print(power_function_s(-2, 2))
start_time = datetime.now()
print(str(power_function_s(7100, 4150))[:50])
end_time = datetime.now()
print(end_time - start_time)
start_time = datetime.now()
print(str(power_function_s_s(7100, 4150))[:50])
end_time = datetime.now()
print(end_time - start_time)





