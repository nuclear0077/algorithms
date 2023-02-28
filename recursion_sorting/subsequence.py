# добавил решение задачи https://contest.yandex.ru/contest/24734/problems/C/
def check_subtext(text, subtext):
    if len(text) == 0 or len(subtext) == 0 or len(subtext) > len(text):
        return False
    count = 0 
    for i in range(len(text)):
        if subtext[count] == text[i]:
            count += 1
            if count == len(subtext):
                return True
    return False


if __name__ == '__main__':
    subtext = input()
    text = input()
    print(check_subtext(text=text, subtext=subtext))