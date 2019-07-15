# incording : utf-8
# add_odd.py

T = int(input())
for test_case in range(1, T + 1):

    list1 = input()
    list1 = list(map(int,list1.split(" ")))

    list2 = [x for x in list1 if x%2 == 1]

    ans = sum(list2)


    print("#{0} {1}".format(test_case, ans))
