# for t in range(int(input())):
for t in range(int(input())):
    a = input()
    for i in range(1,len(a)):
        if a[i:] == a[:-i]:
            print('#{} {}'.format(t+1,i))
            break