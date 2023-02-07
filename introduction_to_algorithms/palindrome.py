import string

# переводим строки в нижний регистр, удаляем пробелы, пунктуацию
# мы должны встать в середину слова ( она разная зависит от четности )  и сделать срез, втору часть слова перевернуть  [::-1]
def main() -> None:
    row = input().lower().replace(' ', '').translate(str.maketrans('', '', string.punctuation))
    if len(row) % 2 == 1:
        mean = len(row) // 2
        print(row[:mean] == row[mean + 1:][::-1])
    else:
        mean = len(row) // 2
        print(row[:mean] == row[mean:][::-1])


if __name__ == '__main__':
    main()