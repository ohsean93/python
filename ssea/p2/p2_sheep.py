T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    ans = 1
    set_a = set()
    set_b = set(list('01234568789'))
    while True:
        m = ans*n
        set_a.update(set(list(str(m))))
        if set_b - set_a == set():
            print('#{} {}'.format(test_case, m*ans))
            break
        ans+=1
