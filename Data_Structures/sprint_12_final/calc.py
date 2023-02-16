# 82380879
# https://contest.yandex.ru/contest/23759/problems/B/
from typing import Dict, Union


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: Union[int, float]) -> None:
        self.items.append(item)

    def pop(self) -> Union[int, float]:
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('pop from empty stack')


class Calculator:
    def __init__(self) -> None:
        self.__stack = Stack()

    def multiply(self) -> None:
        num_second = self.__stack.pop()
        num_first = self.__stack.pop()
        result = num_first * num_second
        self.__stack.push(result)

    def integer_devision(self) -> None:
        num_second = self.__stack.pop()
        num_first = self.__stack.pop()
        result = num_first // num_second
        self.__stack.push(result)

    def subtraction(self) -> None:
        num_second = self.__stack.pop()
        num_first = self.__stack.pop()
        result = num_first - num_second
        self.__stack.push(result)

    def addition(self) -> None:
        num_second = self.__stack.pop()
        num_first = self.__stack.pop()
        result = num_first + num_second
        self.__stack.push(result)

    def push(self, values: Union[int, float]) -> None:
        self.__stack.push(values)

    def pop(self) -> Union[int, float]:
        return self.__stack.pop()


def input_data():
    return input().split()


def run_calcalation_method(calc: Calculator,
                           action: str,
                           value: Union[int, float] = None):
    run_command = getattr(calc, action)
    if action == 'push':
        run_command(value)
    elif action == 'pop':
        print(run_command())
    else:
        run_command()


def run(calc: Calculator, expression):
    actions: Dict[str, str] = {
        '+': 'addition',
        '-': 'subtraction',
        '/': 'integer_devision',
        '//': 'integer_devision',
        '*': 'multiply'
    }
    # :TODO наверное exception надо обработать в цилке? чтобы
    # при повлении ошибки, цикл не прерывался
    for item in expression:
        if item not in actions:
            run_calcalation_method(
                calc=calc, action='push', value=int(item))
            continue
        run_calcalation_method(calc=calc, action=actions.get(item))
    run_calcalation_method(calc=calc, action='pop')


def main():
    calc = Calculator()
    expression = input_data()
    try:
        run(calc=calc, expression=expression)
    except Exception as e:
        print(f'произошла ошибка {e}')


if __name__ == '__main__':
    main()
