def get_factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def sum_odd_numbers(num):
    total = 0
    i = 1
    while i <= num:
        if i % 2 != 0:
            total += i
        i += 1
    return total#
