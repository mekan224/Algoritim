import time
import matplotlib.pyplot as plt
import random

# 1. Линейный поиск
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# 2. Бинарный поиск (работает только на отсортированном массиве)
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Подготовка данных для замеров
sizes = [100, 1000, 10000, 100000, 500000, 1000000]
linear_times = []
binary_times = []

for n in sizes:
    test_list = list(range(n)) # Создаем отсортированный список
    target = -1 # Ищем элемент, которого нет, чтобы замерить ХУДШИЙ случай
    
    # Замер для линейного поиска
    start = time.perf_counter()
    linear_search(test_list, target)
    linear_times.append(time.perf_counter() - start)
    
    # Замер для бинарного поиска
    start = time.perf_counter()
    binary_search(test_list, target)
    binary_times.append(time.perf_counter() - start)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_times, label='Линейный поиск O(n)', marker='o')
plt.plot(sizes, binary_times, label='Бинарный поиск O(log n)', marker='s')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (сек)')
plt.title('Сравнение эффективности алгоритмов поиска')
plt.legend()
plt.grid(True)
plt.show()
