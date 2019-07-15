a = "파이썬"
b = "프로그래밍"
c = "기초"

print(a,b,c)

d = 0.0
print(type(d))

print("%10s" % "우측")
print("%-10s" % "우측")

print("%0.2f" %3.141592)
print("%10.2f" %3.141592)
print("%010.2f" %3.141592)

print("{0:.2}".format(3.141592))
print("{0:0.2}".format(3.141592))
print("{0:10.2}".format(3.141592))


print("이름: {0}, 나이 :  {1} 세".format("홍길동",20))

print("{0:c}, {1}".format(97,97) )

print("이름: %s \n 나이: %s" % ("홍길동",20))
print("이름: %(name)s \n 나이: %(age)s" % {"name":"홍길동","age":20})

print("이름: {name} \n 나이: {age}".format(name="홍길동",age=20) )
print("{0:<10}".format("123"))
print("{0:>10}".format("123"))
print("{0:^10}".format("123"))
print("{0:*^10}".format("123"))
print("{0:1^10}".format("123"))
print("{0:^10}".format("123"))

a = "  hello  "
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.lstrip(" "))
print(a.rstrip(" "))
print(a.strip(" "))
print(a.replace("  ", "\t"))
print(a.replace(" " * 2, "\t"))
print(a.strip().split("e"))
a.isdigit()



# 주석이당