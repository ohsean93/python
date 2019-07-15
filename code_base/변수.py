a=3.14
print(type(a))
a="파리썬"
print(type(a))
a=True
print(type(a))


var1=10
var2=10
print(var1 is var2)
print(var1 == var2)
print(var1 is 10)
print(var1 == 10)

var3=20
print(var1 is var3)
print((var1+var2 )is var3)

#튜플()은 한번 저장되면 변경 불가

#리스트[]는 변경가능 

#셋{}은 중복 허용 않고 인덱스 사용 불가

#딕션어리{}는 키를 이용한 저장
#재입력시 신규키이면 키 추가 동일키면 갱신


student = ("홍길동", 20)

print(student[0])

#student[2]=19 애러뜸

student = ["홍길동", 20]
print(student[0])

student[1] = 19
print(student)
student[1:2] = [19,20]
print(student)

#리스트 항목 추가 방법
student.append("추가")

student.insert(1, 20)
print(student)
student.extend([25, 30])
print(student)
student.append([90, 80])
print(student)

del student[2]
print(student)

print("20 in data_list => {0}".format(20 in student))
print("20 not in data_list => {0}".format(20 not in student))
print("data_list.count(20) => {0}".format(student.count(20)))
print("data_list.count(22) => {0}".format(student.count(22)))

aa = range(1, 11)
bb = [item for item in aa if item % 2 == 0]
cc = [x * y for x in aa if x % 2 == 1
      for y in aa if y % 2 == 0]
print(bb)
print(cc)

'''
age = {20,21,24,21,20}
print(age)

age |= {25,20}
print(age)

dogs = {1:"골든리트리버",2: "진돗개",3:"보더콜리"}
print(dogs)
print(dogs[1])

dogs[2]="바둑이"
dogs[4]="백구"
print(dogs)
'''