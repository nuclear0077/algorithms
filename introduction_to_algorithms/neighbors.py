# https://contest.yandex.ru/contest/23389/problems/C/
def main() -> None:
    n = int(input())
    m = int(input())
    matrix = []
    ans = []
    for i in range(0, n):
        matrix.append(list(map(int, input().split())))
    n_s = int(input())
    m_s = int(input())
    # справа
    if (m_s + 1) >= 0 and (m_s + 1) < m:
        ans.append(matrix[n_s][m_s + 1])
    # слева
    if (m_s - 1) >= 0 and (m_s - 1) < m:
        ans.append(matrix[n_s][m_s - 1])
    # сверху
    if (n_s - 1) >= 0 and (n_s - 1) < n:
        ans.append(matrix[n_s - 1][m_s])
    # снизу
    if (n_s + 1) >= 0 and (n_s + 1) < n:
        ans.append(matrix[n_s + 1][m_s])

    print(*sorted(ans))


if __name__ == '__main__':
    main()
