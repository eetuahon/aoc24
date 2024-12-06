def read_file():
    a = []
    f = open("input06", "r")
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

def task1(f):
    coords = set()
    my = len(f)
    mx = len(f[0])
    x, y = (-1, -1)
    for i in range(my):
        for j in range(mx):
            if f[i][j] == '^':
                x, y = (j, i)
                break
        else:
            continue
        break
    while True:
        while y >= 0 and f[y-1][x] != "#":
            y -= 1
            coords.add((x,y))
        if y < 0: break
        while x < mx - 1 and f[y][x+1] != "#":
            x += 1
            coords.add((x,y))
        if x >= mx - 1: break
        while y < my - 1 and f[y+1][x] != "#":
            y += 1
            coords.add((x,y))
        if y >= my - 1: break
        while x >= 0 and f[y][x-1] != "#":
            x -= 1
            coords.add((x,y))
        if x < 0: break
    print(len(coords)) #6.1

def task2(f):
    coords = set()
    obs = set()
    my = len(f)
    mx = len(f[0])
    x, y = (-1, -1)
    for i in range(my):
        for j in range(mx):
            if f[i][j] == '^':
                x, y = (j, i)
                break
        else:
            continue
        break
    memx, memy = (x, y)
    while True:
        while y > 0 and f[y-1][x] != "#":
            y -= 1
            coords.add((x,y))
        if y <= 0: break
        while x < mx - 1 and f[y][x+1] != "#":
            x += 1
            coords.add((x,y))
        if x >= mx - 1: break
        while y < my - 1 and f[y+1][x] != "#":
            y += 1
            coords.add((x,y))
        if y >= my - 1: break
        while x > 0 and f[y][x-1] != "#":
            x -= 1
            coords.add((x,y))
        if x <= 0: break
    for c in coords:
        if f[c[1]][c[0]] != ".": continue
        temp = set()
        f[c[1]][c[0]] = "#"
        x, y = (memx, memy)
        while True:
            t = len(temp)
            while y > 0 and f[y-1][x] != "#":
                y -= 1
                temp.add((x,y))
            if y <= 0: break
            while x < mx - 1 and f[y][x+1] != "#":
                x += 1
                temp.add((x,y))
            if x >= mx - 1: break
            while y < my - 1 and f[y+1][x] != "#":
                y += 1
                temp.add((x,y))
            if y >= my - 1: break
            while x > 0 and f[y][x-1] != "#":
                x -= 1
                temp.add((x,y))
            if x <= 0: break
            if t == len(temp):
                obs.add(c)
                break
        f[c[1]][c[0]] = "."
    print(len(obs)) #6.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()