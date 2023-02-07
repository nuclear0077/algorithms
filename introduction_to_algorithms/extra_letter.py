def main() -> None:
    s = input()
    t = input()
    s_dict = {}
    t_dict = {}

    for word in s:
        if word in s_dict:
            s_dict[word] += 1
            continue
        s_dict[word] = 1

    for word in t:
        if word in t_dict:
            t_dict[word] += 1
            continue
        t_dict[word] = 1
    for word in t:
        if word not in s_dict:
            print(word)
            continue
        if s_dict[word] != t_dict[word]:
            print(word)
            break


if __name__ == '__main__':
    main()
