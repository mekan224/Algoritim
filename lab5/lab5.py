

n = 0
while n <= 0:
    n = int(input("Введите количество элементов n (n > 0): "))
    if n <= 0:
        print("Ошибка: число должно быть больше нуля.")

array = []
print(f"Введите {n} целых чисел:")
for i in range(n):
    element = int(input(f"Элемент {i}: "))
    array.append(element)

print("Полученный массив:", array)


#второе задание
total_sum = 0
if n > 0:
    max_val = array[0]
    min_val = array[0]

for x in array:
    total_sum += x
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x

average = total_sum / n

print(f"Сумма элементов: {total_sum}")
print(f"Максимальный элемент: {max_val}")
print(f"Минимальный элемент: {min_val}")
print(f"Среднее арифметическое: {average:.2f}")



#третье задание
pos_count = 0
neg_count = 0
even_count = 0

for x in array:
    if x > 0:
        pos_count += 1
    elif x < 0:
        neg_count += 1

    if x % 2 == 0:
        even_count += 1

print(f"Положительных чисел: {pos_count}")
print(f"Отрицательных чисел: {neg_count}")
print(f"Чётных элементов: {even_count}")


#четвертое задания

search_val = int(input("\nВведите число для поиска: "))
found_index = -1

for i in range(len(array)):
    if array[i] == search_val:
        found_index = i
        break

if found_index != -1:
    print(f"Элемент {search_val} найден под индексом {found_index}")
else:
    print(f"Элемент {search_val} в массиве не найден.")

#пятое задание
print("\n--- Задание повышенной сложности ---")
if len(array) < 2:
    print("Ошибка: Для поиска второго максимума нужно минимум 2 элемента.")
else:

    if array[0] > array[1]:
        m1, m2 = array[0], array[1]
    else:
        m1, m2 = array[1], array[0]


    for i in range(2, len(array)):
        if array[i] > m1:
            m2 = m1
            m1 = array[i]
        elif array[i] > m2:
            m2 = array[i]

    print(f"Второй по величине элемент: {m2}")
