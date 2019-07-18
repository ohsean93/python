# incording : utf-8
# max_num.py

T = int(input())
for test_case in range(1, T + 1):

    list1 = input()
    list1 = list(map(int,list1.split(" ")))
    #1 어드 수준
    max_num = max(list1)

    #2 pro 대비용    
    max_num = list1[0]
    for num in list1:
        if max_num < num:
            max_num = num
        
    ans = max_num

    print("#{0} {1}".format(test_case, ans))