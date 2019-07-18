# incording : utf-8
# bigger.py

T = int(input())
for test_case in range(1, T + 1):

    list1 = input()
    list1 = list(map(int,list1.split(" ")))

    if list1[0] < list1[1]:
        ans = "<"
    elif list1[0] > list1[1]:
        ans = ">"
    else:
        ans = "="

    print("#{0} {1}".format(test_case, ans))
