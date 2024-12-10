def read_file():
    a = []
    f = open("input10", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    a = []
    for r in f:
        a.append([int(i) for i in list(r)])
    return a

def find(c, f, l, s, i):
    x, y = (c[0], c[1])
    if x < 0 or y < 0 or x >= len(f[0]) or y >= len(f): return
    if f[y][x] != i: return
    if l[y][x] != 10: return
    l[y][x] = i
    if i == 9: s.add((x,y))
    find((x,y+1), f, l, s, i+1)
    find((x,y-1), f, l, s, i+1)
    find((x+1,y), f, l, s, i+1)
    find((x-1,y), f, l, s, i+1)

def find2(c, f, s, i):
    x, y = (c[0], c[1])
    if x < 0 or y < 0 or x >= len(f[0]) or y >= len(f): return
    if f[y][x] != i: return
    if i == 9: s.append((x,y))
    find2((x,y+1), f, s, i+1)
    find2((x,y-1), f, s, i+1)
    find2((x+1,y), f, s, i+1)
    find2((x-1,y), f, s, i+1)

def task1(f):
    sum = 0
    my = len(f)
    mx = len(f[0])
    zeros = set()
    for y in range(my):
        for x in range(mx):
            if f[y][x] == 0: zeros.add((x,y))
    for c in zeros:
        lab = [[10 for i in range(mx)] for i in range(my)]
        s = set()
        find(c, f, lab, s, 0)
        sum += len(s)
    print(sum) #10.1

def task2(f):
    sum = 0
    my = len(f)
    mx = len(f[0])
    zeros = set()
    for y in range(my):
        for x in range(mx):
            if f[y][x] == 0: zeros.add((x,y))
    for c in zeros:
        s = []
        find2(c, f, s, 0)
        sum += len(s)
    print(sum) #10.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()