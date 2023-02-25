# https://contest.yandex.ru/contest/24734/problems/A/

def bracket_seq(count, string='', left=0, right=0):
    if left == count and right == count:
        print(string)
    else:
        if left < count:
            bracket_seq(count, string + '(', left + 1, right)
        if right < left:
            bracket_seq(count, string + ')', left, right + 1)


def main():
    bracket_seq(count)


if __name__ == '__main__':
    count = int(input())
    bracket_seq(count)