from collections import defaultdict

def read_file():
    a = []
    f = open("input11", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    return [int(i) for i in f[0].split()]

def divisible(i):
    str_n = str(i)
    l = len(str_n)
    if l % 2 != 0:
        return False
    return (int(str_n[:l // 2]), int(str_n[l // 2:]))

def stone_counter(f, blinks):
    s = 0
    for i in range(blinks):
        temp = defaultdict(lambda: 0)
        for k in f.keys():
            if k == 0:
                temp[1] += f[0]
            elif divisible(k):
                a,b = divisible(k)
                temp[a] += f[k]
                temp[b] += f[k]
            else:
                temp[k * 2024] += f[k]
        f = temp
    for k in f.keys():
        s += f[k]
    return s

def task1(f):
    c = defaultdict(lambda: 0)
    for i in f:
        c[i] += 1
    sum = stone_counter(c, 25) # After 25 blinks asked
    print(sum) #11.1

def task2(f):
    c = defaultdict(lambda: 0)
    for i in f:
        c[i] += 1
    sum = stone_counter(c, 75) # After 75 blinks asked
    print(sum) #11.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()