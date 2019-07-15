# incording : utf-8
# p1_ymd.py

T = int(input())
for test_case in range(1, T + 1):

    list1 = input()
    year = str(list1[0:4])
    month = str(list1[4:6])
    day = str(list1[6:])
    month_int = int(month)
    day_int = int(day)

    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]

    check = 1

    if month_int in day_30:
        if day_int <= 30:
            check = 0
        else:
            ans = -1

    elif month_int in day_31:
        if day_int <= 31:
            check = 0
        else:
            ans = -1

    elif month_int == 2:
        if day_int <= 28:
            check = 0
        else:
            ans = -1

    if check == 0:
        ans = "{0}/{1}/{2}".format(year, month, day)

    print("#{0} {1}".format(test_case, ans))