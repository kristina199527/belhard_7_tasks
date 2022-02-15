"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""
import random


class RandSequence:
    n: int
    sequence: list[int]

    def __init__(self, n: int):
        self.n = n
        self.generate()

    def generate(self, n: int = None):
        n = n or self.n
        self.sequence = [random.randint(-n, n) for _ in range(n)]

    def print_seq(self):
        print(self.sequence)
