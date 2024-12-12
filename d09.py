from collections import deque, defaultdict

def read_file():
    a = []
    f = open("input09", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def task1(f):
    f = [int(i) for i in list(f[0])]
    sum = 0
    mid = len(f) // 2
    id = 0
    i, j = (0, len(f)-1)
    if len(f) % 2 == 0:
        j -= 1
        mid -= 1
    dq = deque()
    q = []
    extra = 0
    while i <= j:
        if i % 2 == 0:
            for x in range(f[i]):
                q.append(id)
            id += 1
        else:
            while len(dq) < f[i] and i <= j:
                for x in range(f[j]):
                    dq.append(mid)
                extra += f[j]
                mid -= 1
                j -= 2
            for x in range(f[i]):
                if len(dq) > 0:
                    q.append(dq.popleft())
                    extra -= 1
        i += 1
    while len(dq) > 0 and extra > 0:
        q.append(dq.popleft())
        extra -= 1
    for i in range(len(q)):
        sum += i * q[i]
    print(sum) #9.1

def task2(f):
    sum = 0
    f = [int(i) for i in list(f[0])]
    rr = dict()
    priority = []
    id = 0
    for i in range(0, len(f),2):
        l = f[i]
        rr[id] = l
        priority.insert(0,id)
        id += 1
    q = []
    id = 0
    for i in range(len(f)):
        n = f[i]
        if i % 2 == 0:
            if id in priority:
                for x in range(n):
                    q.append(id)
                priority.remove(id)
            else:
                r = rr[id]
                while r > 0:
                    ind = 0
                    while ind < len(priority) and rr[priority[ind]] > n:
                        ind += 1
                    if ind < len(priority):
                        no = priority[ind]
                        priority.remove(no)
                        for z in range(rr[no]):
                            q.append(no)
                        r -= rr[no]
                    else:
                        for z in range(n):
                            q.append(0)
                            r -= 1
            id += 1
        else:
            while n > 0:
                ind = 0
                while ind < len(priority) and rr[priority[ind]] > n:
                    ind += 1
                if ind < len(priority):
                    no = priority[ind]
                    priority.remove(no)
                    for z in range(rr[no]):
                        q.append(no)
                    n -= rr[no]
                else:
                    for z in range(n):
                        q.append(0)
                        n -= 1
    for i in range(len(q)):
        sum += i * q[i]
    print(sum) #9.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()