def main():
    print('Diamonds')

    # Display diamonds of sizes 0 through 6:
    for diamondSize in range(0, 6):
        displayOutlineDiamond(diamondSize)
        print()
        displayFilledDiamond(diamondSize)
        print()

def displayOutlineDiamond(size):
    # Display the top half of the diamond:
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/', end='')
        print(' ' * (i * 2), end='')
        print('\\')

    for i in range(size):
        print(' ' * i, end='')
        print('\\', end='')
        print(' ' * ((size - i - 1) * 2), end='')
        print('/')

def displayFilledDiamond(size):
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/' * (i + 1), end='')
        print('\\' * (i + 1))

    for i in range(size):
        print(' ' * i, end='')
        print('\\' * (size - i), end='')
        print('/' * (size - i))

if __name__ == '__main__':
    main()
