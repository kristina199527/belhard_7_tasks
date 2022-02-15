"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: float

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __ne__(self, other):
        return self.average_score != other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __gt__(self, other):
        return self.average_score > other.average_score

    def __ge__(self, other):
        return self.average_score >= other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score


KS = Student("Cуховская", "Кристина", 7, 8.5)
GY = Student("Герасимчик", "Ярослав", 7, 6.9)
PV = Student("Прохорсик", "Владимир", 7, 8.2)
BG = Student('Боровская', 'Галина', 7, 9.2)
ND = Student('Нахват', 'Дмитрий', 7, 4.9)

some_list = [KS, GY, PV, BG, ND]
print(sorted(some_list))

some_list_2 = []
for i in some_list:
    if i.average_score > 5:
        some_list_2.append(i)
print(some_list_2)
