import re

def read_file():
    a = []
    f = open("input03", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def task1(f):
    sum = 0
    input = "".join(f)
    ls = re.findall("mul[(]\d+[,]\d+[)]",input)
    for mul in ls:
        n = [int(i) for i in re.findall("\d+",mul)]
        sum += n[0] * n[1]
    print(sum) #3.1

def task2(f):
    sum = 0
    input = "".join(f)
    while "don\'t()" in input:
        dont = input.split("don\'t()",1)
        do = dont[1].split("do()",1)
        if len(do) == 2:
            input = dont[0] + do[1]
        else:
            input = dont[0]
    ls = re.findall("mul[(]\d+[,]\d+[)]",input)
    for mul in ls:
        n = [int(i) for i in re.findall("\d+",mul)]
        sum += n[0] * n[1]
    print(sum) #3.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()