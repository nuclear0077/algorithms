# https://contest.yandex.ru/contest/23758/problems/A/

def transported(matrix_input, matrix_lines, matrix_columns):
    transported_matrix = []
    for _ in range(matrix_columns):
        transported_matrix.append([0] * matrix_lines)
    for i in range(matrix_columns):
        for j in range(matrix_lines):
            transported_matrix[i][j] = matrix_input[j][i]
    return transported_matrix


def main() -> None:
    matrix_lines = int(input())
    matrix_columns = int(input())
    matrix_input = [input().split(' ') for _ in range(matrix_lines)]
    transported_matrix = transported(
        matrix_input=matrix_input,
        matrix_lines=matrix_lines,
        matrix_columns=matrix_columns)
    for matrix in transported_matrix:
        print(*matrix)


if __name__ == '__main__':
    main()