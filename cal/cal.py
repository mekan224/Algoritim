a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
op = input("Операция (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Деление на ноль")
else:
    print("Неизвестная операция")
