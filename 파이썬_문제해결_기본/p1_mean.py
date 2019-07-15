# incording : utf-8
# mean.py

T = int(input())
for test_case in range(1, T + 1):

    list1 = input()
    list1 = list(map(int,list1.split(" ")))

    ans = (sum(list1)/len(list1)+0.5)//1

    print("#{0} {1}".format(test_case, ans))
