n = 9


for n1 in range(1, n):
    for n2 in range(n1 + 1, n):
        if n % (n1 + n2) == 0:
            print(f'{n1}{n2}', end='')
