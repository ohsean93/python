T = int(input())
for test_case in range(1, T + 1):
    list1 = input()
    k, n, m = list1.split(" ")
    list2 = input()
    list_bus_stop = list(map(int,list2.split(" ")))

    k = int(k)
    n = int(n)
    m = int(m)

    start = 0
    mid = k
    end = n
    ans = 0

    while mid < n:

        check = 1
        next_start = start
        for i in range(start, mid + 1):
            if list_bus_stop[0] == i:
                list_bus_stop.pop(0)
                check = 0
                next_start = i

        if check != 0:
            ans = 0
            break
        else:
            ans += 1
            start = next_start
            mid = start + k

    print("#{0} {1}".format(test_case, ans))


