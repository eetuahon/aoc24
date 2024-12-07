def read_file():
    a = []
    f = open("input07", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    n = []
    for r in f:
        a = r.split(": ")
        n.append((int(a[0]), [int(i) for i in a[1].split()]))
    return n

def operations(t, c, n, i):
    if i == len(n) - 1:
        if c + n[i] == t or c * n[i] == t:
            return True
        else: return False
    elif c > t:
        return False
    else:
        return operations(t, c + n[i], n, i + 1) or operations(t, c * n[i], n, i + 1)

def trunc(a, b):
    n = b
    while (n > 0):
        a *= 10
        n //= 10
    return a + b

def operations2(t, c, n, i):
    if i == len(n) - 1:
        if c + n[i] == t or c * n[i] == t or trunc(c, n[i]) == t:
            return True
        else: return False
    elif c > t:
        return False
    else:
        return operations2(t, c + n[i], n, i + 1) or operations2(t, c * n[i], n, i + 1) or operations2(t, trunc(c, n[i]), n, i + 1)

def task1(f):
    sum = 0
    for r in f:
        target = r[0]
        nums = r[1]
        if operations(target, nums[0], nums, 1): sum += target
    print(sum) #7.1

def task2(f):
    sum = 0
    for r in f:
        target = r[0]
        nums = r[1]
        if operations2(target, nums[0], nums, 1): sum += target
    print(sum) #7.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()