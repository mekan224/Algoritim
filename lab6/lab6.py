import random

# ===== ВВОД РАЗМЕРОВ =====
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# ===== СОЗДАНИЕ МАТРИЦЫ =====
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 20))
    matrix.append(row)

# ===== ВЫВОД МАТРИЦЫ =====
print("\nМатрица:")
for row in matrix:
    for value in row:
        print(f"{value:4}", end="")
    print()

# ===== ЗАДАНИЕ 1 =====
total = 0
maximum = matrix[0][0]

for row in matrix:
    for value in row:
        total += value
        if value > maximum:
            maximum = value

print("\nСумма всех элементов:", total)
print("Максимальный элемент:", maximum)

# ===== ЗАДАНИЕ 2 =====

# Сумма по строкам
row_sums = []
print("\nСуммы по строкам:")
for i in range(rows):
    row_sum = 0
    for j in range(cols):
        row_sum += matrix[i][j]
    row_sums.append(row_sum)
    print(f"Строка {i}: {row_sum}")

# Сумма по столбцам
print("\nСуммы по столбцам:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Столбец {j}: {col_sum}")

# Строка с максимальной суммой
max_row_index = row_sums.index(max(row_sums))
print("Строка с максимальной суммой:", max_row_index)

# ===== ЗАДАНИЕ 3 =====

def shift_right(row):
    new_row = []
    
    # Добавляем только ненулевые элементы
    for x in row:
        if x != 0:
            new_row.append(x)
    
    # Добавляем нули слева
    zeros_count = len(row) - len(new_row)
    zeros = [0] * zeros_count
    
    return zeros + new_row


print("\n=== Мини-проект 4x4 ===")

field = [
    [0, 2, 0, 4],
    [1, 0, 3, 0],
    [0, 0, 5, 6],
    [7, 0, 0, 8]
]

print("До сдвига:")
for row in field:
    print(row)

for i in range(4):
    field[i] = shift_right(field[i])

print("\nПосле сдвига вправо:")
for row in field:
    print(row)