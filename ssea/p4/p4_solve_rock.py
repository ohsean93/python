T= int(input())
for test_case in range(1, T + 1):
    n, m = tuple(map(int, input().split(' ')))
    add_value = 0

    for i in range(n+1):
        mid_value = (n-i)**m * (-1)**(i % 2)

        for j in range(1, i+1):
            mid_value *= n - j + 1
        for j in range(1,i+1):
            mid_value = mid_value // j

        add_value+=mid_value
    ans = add_value % 1000000007
    print('#{0} {1}'.format(test_case, ans))