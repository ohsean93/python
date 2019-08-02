for i in(int(input())):
        a=input()
        if a[::-1] == a:
                print('#{} {}'.format(i+1,1))
        else:
                print('#{} {}'.format(i+1,0))