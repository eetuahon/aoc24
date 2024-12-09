from collections import deque, defaultdict

def read_file():
    a = []
    f = open("input09", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def task1(f): # I mean this takes long
    f = [int(i) for i in list(f[0])]
    sum = 0
    id = 0
    i = 0
    dq = deque()
    s = dict()
    for v in range(len(f)):
        n = int(f[v])
        if v % 2 == 0:
            for x in range(n):
                s[i] = id
                i += 1
            id += 1
        else:
            for x in range(n):
                dq.append(i)
                i += 1
    temp1, temp2 = (0,0)
    while max(s.keys()) > len(s) - 1:
        m = max(s.keys())
        temp1 = dq[0]
        temp2 = m
        s[dq.popleft()] = s[m]
        del s[m]
    for k in s.keys():
        sum += k * s[k]
    print(sum) #9.1

def task2(f): # and this, I'll improve if I have time at some point
    f = [int(i) for i in list(f[0])]
    sum = 0
    id = 0
    i = 0
    s = dict()
    e = dict()
    r = dict()
    finder = defaultdict(lambda: list())
    for v in range(len(f)):
        n = int(f[v])
        if v % 2 == 0:
            for x in range(n):
                s[i] = id
                finder[id].append(i)
                i += 1
            r[id] = n
            id += 1
        else:
            while n > 0:
                e[i] = n
                i += 1
                n -= 1
    id -= 1
    while id >= 0:
        rr = r[id]
        for er in sorted(e.keys()):
            if er > finder[id][0]: continue
            if e[er] >= rr:
                while rr > 0:
                    s[er] = id
                    e[er] = 0
                    er += 1
                    rr -= 1
                for k in finder[id]:
                    s[k] = -1
        id -= 1
    for k in s.keys():
        if s[k] != -1: sum += k * s[k]
    print(sum) #9.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()