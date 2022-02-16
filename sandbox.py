def main():

    for i in range(-3, 4, 2):
        print(i, end=':')
    print()

    # b
    for z in range(5):
        print(5, end='')
    print()

    # c
    phrase = "hello"
    for x in phrase:
        print(x, end='--')
    print("END")

    # d
    phrase = "hope"
    for c in phrase:
        print(c * 4, end=' ')
    print()

    # e
    string = "Last Jedi"
    x = 0
    for s in string:
        print(x, s, end=' ')
        x += 1
    print()

    # f
    for r in range(45, -45, -25):
        print(r, end='|')
    print()

    # g
    for q in range(34, 5):
        print(q)


main()
