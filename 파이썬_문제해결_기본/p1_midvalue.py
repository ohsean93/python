# incording : utf-8
# midvalue.py

num = int(input())
list1 = input()
list1 = list(map(int,list1.split(" ")))

#어드용
ans = sorted(list1)[int(num//2)]


#pro 대비
for i in range(num):
    for j in range(num-i-1):
        if list1[j] > list1[j+1]:
            t = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = t

    
ans2 = list1[int(num//2)]

print(ans) 
print(ans2)