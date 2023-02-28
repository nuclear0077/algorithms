# https://contest.yandex.ru/contest/24734/problems/N/


# Создаем список (например, intervals) и добавляем в него все отрезки, заданные во входных данных.
# Сортируем список intervals по начальным координатам отрезков.
# Создаем пустой список (например, result), который будет содержать границы клумб.
# Проходимся по списку intervals и для каждого отрезка проверяем, сливается ли он с предыдущим отрезком (т.е. перекрывается ли он с ним). Если да, то объединяем их в один отрезок и продолжаем проверку с новым объединенным отрезком.
# Если отрезок не сливается с предыдущим, то добавляем границы предыдущего отрезка в список result и продолжаем проверку с новым отрезком.
# После завершения цикла добавляем границы последнего отрезка в список result.
# Сортируем список result и выводим каждый элемент списка на новой строке.


def flowerbed(intervals):
    # Список для хранения результирующих клумб
    flowers = []

    # Начинаем первую клумбу с первого отрезка
    curr_start, curr_end = intervals[0]

    for i in range(1, n):
        start, end = intervals[i]
        if start <= curr_end:
            # Если текущий отрезок пересекается с предыдущим,
            # то объединяем их
            curr_end = max(curr_end, end)
        else:
            # Иначе добавляем предыдущую клумбу и начинаем новую
            flowers.append((curr_start, curr_end))
            curr_start, curr_end = start, end

    # Добавляем последнюю клумбу
    flowers.append((curr_start, curr_end))

    # Выводим координаты клумб в отсортированном порядке
    for start, end in flowers:
        print(start, end)


if __name__ == '__main__':
    n = int(input())
    intervals = []
    for i in range(n):
        start, end = map(int, input().split())
        intervals.append((start, end))

    #Сортируем отрезки по начальной координате
    intervals.sort()
    flowerbed(intervals)