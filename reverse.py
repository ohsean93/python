with open("problem.txt", "w") as f:
    for i in range(4):
        f.write(f"{i}\n")



with open("problem.txt", "w") as f:
    for i in range(4):
        f.write(f"{3-i}\n")


with open("reverse.txt", "w") as f1:
    with open("problem.txt", "r") as f2:
        list1 = f2.readlines()
        list1.reverse()
        f1.writelines(list1)

