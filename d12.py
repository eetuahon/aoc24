from collections import deque

def read_file():
    a = []
    f = open("input12", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    a = []
    for r in f:
        a.append(list(r))
    return a

def search(f, b, c, p, contribution):
    x, y = c
    area = 1
    border = contribution[(x,y)]
    b[y][x] = True
    dq = deque()
    dq.append(c)
    while len(dq) > 0:
        cn = dq.popleft()
        cx, cy = (cn[0], cn[1])
        for dx, dy in [(cx-1, cy),(cx,cy-1),(cx+1,cy),(cx,cy+1)]:
            if dx >= 0 and dx < len(f[0]) and dy >= 0 and dy < len(f) and not b[dy][dx] and f[dy][dx] == p:
                b[dy][dx] = True
                dq.append((dx,dy))
                area += 1
                border += contribution[(dx,dy)]
    return (area, border)

def task1(f):
    sum = 0
    contribution = dict()
    mx, my = (len(f[0]), len(f))
    for y in range(my):
        for x in range(mx):
            p = f[y][x]
            b = 4
            if x > 0 and f[y][x-1] == p: b -= 1
            if y > 0 and f[y-1][x] == p: b -= 1
            if x < mx - 1 and f[y][x+1] == p: b -= 1
            if y < my - 1 and f[y+1][x] == p: b -= 1
            contribution[(x, y)] = b
    been = [[False for i in range(mx)] for i in range(my)]
    for y in range(my):
        for x in range(mx):
            if been[y][x]: continue
            p = f[y][x]
            gs = search(f, been, (x,y), p, contribution)
            sum += gs[0] * gs[1]
    print(sum) #12.1

def task2(f):
    sum = 0
    contribution = dict()
    borders = dict()
    mx, my = (len(f[0]), len(f))
    for y in range(my):
        for x in range(mx):
            p = f[y][x]
            b = [True, True, True, True]
            c = 4
            if x > 0 and f[y][x-1] == p:
                b[0] = False
                c -= 1
            if y > 0 and f[y-1][x] == p:
                b[1] = False
                c -= 1
            if x < mx - 1 and f[y][x+1] == p:
                b[2] = False
                c -= 1
            if y < my - 1 and f[y+1][x] == p:
                b[3] = False
                c -= 1
            borders[(x,y)] = b
            if x > 0 and b[1] and borders[(x-1,y)][1] and f[y][x-1] == p:
                c -= 1
            if y > 0 and b[0] and borders[(x,y-1)][0] and f[y-1][x] == p:
                c -= 1
            if x > 0 and b[3] and borders[(x-1,y)][3] and f[y][x-1] == p:
                c -= 1
            if y > 0 and b[2] and borders[(x,y-1)][2] and f[y-1][x] == p:
                c -= 1
            contribution[(x, y)] = c
    been = [[False for i in range(mx)] for i in range(my)]
    for y in range(my):
        for x in range(mx):
            if been[y][x]: continue
            p = f[y][x]
            gs = search(f, been, (x,y), p, contribution)
            sum += gs[0] * gs[1]
    print(sum) #12.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()