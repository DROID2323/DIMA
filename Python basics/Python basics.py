# Основні типи даних

a = "змінна з текстом"
b = 1  # числова змінна
b1 = 1.1  # дійсне число
c = ["a", 1, 1.25, "Слово", a]  # список (list)
d = {"a": "Слово", "b": 1, a: b}  # словник (dict)
e = ("a", a)  # кортеж (tuple)
f = {"ss", str(b) + a}  # множина (set)

print("a =", a)
print("b =", b)
print("Список:", c)
print("Словник:", d)
print("Кортеж:", e)
print("Множина:", f)

# ------------------------
# 2. Вбудовані константи та зарезервовані слова
# ------------------------
print("Перша константа:", True)
print(f"Як можна так робити вивід? {False}")

import sys
help("keywords")

# ------------------------
# 3. Вбудовані функції
# ------------------------
print(abs(-12.5), "є рівним", abs(12.5))
print("Максимум із 1, 2, 3:", max(1, 2, 3))
print("Мінімум із 5, 7, 9:", min(5, 7, 9))
print("Сума елементів:", sum([1, 2, 3, 4, 5]))

# ------------------------
# 4. Цикли (for, while)
# ------------------------
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")
else:
    print("Кінець циклу for!")

count = 0
while count < 3:
    print("Рахунок:", count)
    count += 1

# ------------------------
# 5. Розгалуження (if-else)
# ------------------------
from random import randint
A = randint(0, 1)
print(f"Значить A={A}" if A else f"Але може бути що A={A}")

B = 5
if B > 0:
    print("B додатне")
elif B == 0:
    print("B дорівнює нулю")
else:
    print("B від’ємне")

# ------------------------
# 6. try → except → finally
# ------------------------
A = 0
try:
    print("Що буде якщо", 10 / A, "?")
except Exception as e:
    print("Невже це помилка >", e)
finally:
    print("О це так на тобі!")

# ------------------------
# 7. Контекст-менеджер with
# ------------------------
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Це тестовий файл!\nPython працює!")

with open("example.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        print(f"{i + 1}) {line.strip()}")

# ------------------------
# 8. Лямбда-функції
# ------------------------
def a_b_func(a, b):
    return a, b

this_is_lambda = lambda first, age: f"Цей код написав: {first}, мені {age} років"

print("Це просто функція:", a_b_func("x", "y"))
print("А це лямбда:", this_is_lambda("Богдан", 18))
print(this_is_lambda(*a_b_func("Python", 30)))

# ------------------------
# 9. Приклад відповіді від AI
# ------------------------
name = input("Введіть ваше ім'я: ")
print(f"Привіт, {name}! Вітаю у світі Python 🐍")

for i in range(3):
    print(f"Цикл номер {i + 1}")