T=int(input())
matrix = []
small_s = [[0,1,2],[3,4,5],[6,7,8]]
check = set('123456789')
for test_case in range(T):
	matrix.clear()
	c = 1
    for num in range(9):
        line = input().split(' ')
        if check - set(line) != set():
            c = 0
        matrix.append(line)


    for j in range(9):
        cal = [x[j] for x in matrix]
        if check - set(cal) != set():
            c = 0
        cal = []

    square = []
    for m in small_s:
        for n in small_s:
            square.clear()
            for i in n:
                for j in m:
                    square.append(matrix[i][j])
            if check - set(square) != set():
                c = 0
                
	if c == 1:
        print('#{} 1'.format(test_case+1))
	else:
		print('#{} 0'.format(test_case+1))