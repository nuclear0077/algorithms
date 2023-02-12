# Идем по списку последовательности
# если встречаем открывающиеся скобки, кладем в стек
# если встречаем закрывающиеся скобки, проверяем,
# что стек не пустой, если пустой return False
# далее получим значение из стека, проверяем если текущий
# закрывающийся символ = открывающемуся символу,
# то это правильно последовательность, иначе возвращаем False
# если прошли весь цикл и не вышли из функции а последвательность пустая,
# возвращаем True, иначе False
def is_correct_bracket_seq():
    seq_symbol = input()
    stack = []
    open_seq = '({['
    for symbol in seq_symbol:
        if symbol in open_seq:
            stack.append(symbol)
        else:
            if not stack:
                return False
            left_symbol = stack.pop()
            if left_symbol == '(' and symbol == ')':
                continue
            if left_symbol == '[' and symbol == ']':
                continue
            if left_symbol == '{' and symbol == '}':
                continue
            else:
                return False
    return stack == []


if __name__ == '__main__':
    print(is_correct_bracket_seq())
