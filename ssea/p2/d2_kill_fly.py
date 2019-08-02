T = int(input())
matrix = []
for test_case in range(T):
    n, m = tuple(map(int,input().split(' ')))
    matrix.clear()
    for row in range(n):
        matrix.append(list(map(int,input().split(' '))))

    max_kill_count = 0
    for point_x in range(n-m+1):
        for point_y in range(n-m+1):
            kill_count=0
            for kill_row in range(m):
                kill_count += sum(matrix[point_y+kill_row][point_x:point_x+m])
            if max_kill_count < kill_count:
                max_kill_count = kill_count

    print('#{} {}'.format(test_case+1,max_kill_count))