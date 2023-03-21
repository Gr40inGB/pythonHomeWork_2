# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input('Please input amount coins: '))
s = []
for x in range(n):
    s.append("Eagle" if random.randint(0, 1) else "Tail")
    print(s[x], end=" ")

eagle = s.count("Eagle")
tail = s.count("Tail")
if eagle < tail:
    print(f"\nWe need flip {eagle} eagle coin")
else:
    print(f"\nWe need flip {tail} tail coin")
