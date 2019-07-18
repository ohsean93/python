
T = int(input())
for test_case in range(1, T + 1):
    T = int(input())
    list1 = list(input())
    index = list("9876543210")
    max_count = 0

    for i in index:
        count = list1.count(i)

        if count > max_count:
            num = i
            max_count = count

    print("#{0} {1} {2}".format(test_case, num, max_count))