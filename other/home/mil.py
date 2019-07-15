T = int(input())

for test_case in range(1, T+1):
    days = int(input())
    price = input().split()
    price = list(map(int, price))

    pick_day = []
    pick_price = []

    for i in range(1,days-1):
        if ((price[i-1] <= price[i]) and (price[i] > price[i+1])):
            pick_day.append(i)
            pick_price.append(price[i])
    
    pick_day.append(days-1)
    pick_price.append(price[-1])

    sum_price = 0

    a = 0
    index = 0
    
    for i in pick_day:
        for j in range(a, i):
            max_price= max(pick_price[index:])
            if price[j] < max_price:
                sum_price += max_price - price[j]
        index += 1
        a = int(i)


    print("#{0} {1}".format(test_case, sum_price))
    
    price.clear()
   
