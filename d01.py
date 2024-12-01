def read_file():
    a = []
    f = open("input01", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def modify_file(f):
    first = []
    second = []
    for r in f:
        a = r.split("   ")
        first.append(int(a[0]))
        second.append(int(a[1]))
    return (first, second)

def task1(f):
    sum = 0
    first = f[0]
    second = f[1]
    first.sort()
    second.sort()
    for i in range(len(first)):
        sum += abs(second[i] - first[i])
    print(sum) #1.1

def task2(f):
    sum = 0
    first = f[0]
    second = f[1]
    first.sort()
    second.sort()
    j = 0
    for i in range(len(first)):
        if i > 0 and first[i] == first[i-1]:
            continue
        s = 0
        while j < len(first) - 1 and second[j] < first[i]:
            j += 1
        while second[j] == first[i]:
            s += first[i]
            j += 1
        c = 1
        while i < len(first) - 1 and first[i+1] == first[i]:
            c += 1
            i += 1
        sum += s * c
    print(sum) #1.2

def main():
    f = read_file()
    f = modify_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()