#
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import random


def terrible_search(a, b):
    for i in range(1, 1001):
        for j in range(1, 1001):
            if i * j == a and i + j == b:
                print(i, j)
                return


def square_roots(a, b):  # x**2 - a*x + b = 0
    x1 = (-(-a) + (a ** 2 - 4 * 1 * b) ** 0.5) / 2
    x2 = (-(-a) - (a ** 2 - 4 * 1 * b) ** 0.5) / 2
    print(int(x2), int(x1))


print('Petya conceive a numbers X, Y')
x, y = random.randint(1, 1000), random.randint(1, 1000)
print(f"Petya say: x * y = {x * y}, x + y = {x + y}")

terrible_search(x * y, x + y)

square_roots(x + y, x * y)