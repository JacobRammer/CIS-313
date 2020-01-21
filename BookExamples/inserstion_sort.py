a = [5, 2, 4, 6, 1, 3]


def main():
    for j in range(1, len(a)):
        test = a
        key = a[j]
        i = j - 1
        test2 = a[i]
        while i >= 0 and key < a[i]:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key

    for i in a:
        print(i)


main()
