r = 2


def pw(x):
    p = 1 / x
    return p


def rt(y, z):
    c = 0
    t = y
    for i in range(2, 9999):
        a = pow(y, z)
        y = a
        c += 1
        if a == 1:
            break
    z += 1
    if r == 2:
        print('\nAfter taking \'', c, '\'', 'Square roots', t, 'becomes 1 \n')
    else:
        if r == 3:
            print('\nAfter taking \'', c, '\'', 'Cube roots', t, 'becomes 1 \n')
        else:
            print('\nAfter taking \'', c, '\'', r, 'th roots', t, 'becomes 1 \n')
    return


num = int(input('Enter a number: '))
n = int(input('Enter the nth root: '))
n += 1
for j in range(2, n):
    rt(num, pw(j))
    r += 1
