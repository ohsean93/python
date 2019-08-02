T = int(input())
matrix = []
for test_case in range(T):
    n = int(input())
    matrix.clear()
    for line in range(n):
        sub = []
        for row in range(n):
            sub.append(0)
        
        matrix.append(sub)
	
    add_vactor = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    vactor_check = 0
    len_vactor = n
    real_len = 0
    len_vactor_check = 1
    line, row = 0, 0
    for i in range(1, n**2+1):
        matrix[line][row] = str(i)
        real_len +=1
        if len_vactor == real_len:
            vactor_check +=1
            vactor_check %=4
            len_vactor_check += 1
            if len_vactor_check == 2:
                len_vactor -=1
                len_vactor_check = 0
            real_len = 0

        line += add_vactor[vactor_check][1]
        row += add_vactor[vactor_check][0]

    print('#{}'.format(test_case+1))
    for line in range(n):
        print(' '.join(matrix[line]))
