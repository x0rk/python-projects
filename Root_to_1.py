r = 2

def root(y, z):
    c = 0
    t = y
    while True:
        y = a = pow(y, z)
        c += 1
        if a == 1:
            break
    if r == 2:
        print('\nAfter taking \'', c, '\'', 'Square roots', t, 'becomes 1\n')
    elif r == 3:
        print('\nAfter taking \'', c, '\'', 'Cube roots', t, 'becomes 1\n')
    else:
        print('\nAfter taking \'', c, '\'', r, 'th roots', t, 'becomes 1\n')

num = int(input('Enter a number: '))
n = int(input('Enter the nth root: '))

for j in range(2, n+1):
    root(num, 1/j)
    r += 1
