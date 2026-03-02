# ==============================
# Лабораторная работа №7
# ==============================

# Задание 1

def add(a, b):
    return a + b


def power(a, n=2):
    return a ** n


def sum_all(*args):
    total = 0
    for value in args:
        total += value
    return total


# Задание 2

count = 10

def change_value():
    global count
    count = 20


# Задание 3

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Задание 4

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


# Задание 5

def max_element(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]

    max_rest = max_element(arr, index + 1)

    if arr[index] > max_rest:
        return arr[index]
    else:
        return max_rest


# Дополнительно

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_fast(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def average(a, b, c):
    return (a + b + c) / 3


def is_even(n):
    return n % 2 == 0


def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)


def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


def fast_power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half = fast_power(a, n // 2)
        return half * half
    else:
        return a * fast_power(a, n - 1)


def count_depth(n):
    if n == 0:
        return 1
    return 1 + count_depth(n - 1)


# Проверка

if __name__ == "__main__":

    print(add(3, 5))
    print(power(4))
    print(sum_all(1, 2, 3))

    print("До:", count)
    change_value()
    print("После:", count)

    print(factorial_recursive(5))
    print(factorial_iterative(5))

    print(sum_digits(1234))

    numbers = [3, 7, 2, 9, 5]
    print(max_element(numbers))

    print(fibonacci(6))
    print(fibonacci_fast(6))

    print(average(3, 6, 9))
    print(is_even(4))

    print(is_palindrome("level"))

    print(fast_power(2, 10))

    print(count_depth(5))

    print_numbers(5)