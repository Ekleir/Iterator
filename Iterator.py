class ListOfNumbers:
    """Принимает числа для проверки итерации"""

    def __init__(self, *list_of_numbers: int):
        self.list_of_numbers = list(list_of_numbers)

    def __str__(self):
        return f'Список из элементов: {self.list_of_numbers}'

    def __iter__(self):
        return IteratorByTen(self.list_of_numbers)


class IteratorByTen:
    """Итератор для умножения значения на 10"""

    def __init__(self, numbers: ListOfNumbers):
        self.numbers = numbers
        self.cursor = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.cursor < len(self.numbers):
            num_res = self.numbers[self.cursor] * 10
            self.cursor += 1
            return num_res
        raise StopIteration


if __name__ == '__main__':
    a = ListOfNumbers(2, 3, 1, 5)

    for el in a:
        print(el)