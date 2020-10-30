#!/usr/bin/python3

# Задание 12 - Факториал

print("12. Факториал")


def fuckt(n):
    if (n < 0):
        return 0
    else:
        return 1 if n == 0 else n * fuckt(n - 1)


print(fuckt(int(input('Факториал числа: '))))
