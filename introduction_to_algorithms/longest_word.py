# https://contest.yandex.ru/contest/23389/problems/E/
# на вход получаем строк,  конвертируем ее в список
# инициализируем переменную длинны и сохранения слова
# идем в цикле по элементам списка и проверяем, если curr_word > longest word, записываем значения,  далее выводим 
def main() -> None:
    n = int(input())
    text = input()
    longest_word = None
    long_word = 0
    for word in text.split():
        if len(word) > long_word:
            longest_word = word
            long_word = len(word)
    print(longest_word)
    print(long_word)


if __name__ == '__main__':
    main()
