def main() -> None:
    numbers = list(map(int, input().split()))

    leftovers = []

    for num in numbers:
        leftovers.append(num % 2)

    if sum(leftovers) == 3 or sum(leftovers) == 0:
        print('WIN')
    else:
        print('FAIL')


if __name__ == '__main__':
    main()
