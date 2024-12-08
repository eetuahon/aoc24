from collections import defaultdict

def read_file():
    a = []
    f = open("input08", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def antenna_coords(f):
    antennas = defaultdict(lambda: list())
    for y in range(len(f)):
        for x in range(len(f[0])):
            if f[y][x] != ".": antennas[f[y][x]].append((x,y))
    return antennas

def task1(f):
    coords = set()
    my = len(f)
    mx = len(f[0])
    antennas = antenna_coords(f)
    for l in antennas.values():
        for i in range(len(l)):
            for j in range(len(l)):
                if i == j: continue
                a,b = (l[i], l[j])
                cx = 2 * a[0] - b[0]
                if cx >= mx or cx < 0: continue
                cy = 2 * a[1] - b[1]
                if cy < my and cy >= 0: coords.add((cx,cy))
    print(len(coords)) #8.1

def task2(f):
    coords = set()
    my = len(f)
    mx = len(f[0])
    antennas = antenna_coords(f)
    for l in antennas.values():
        for i in range(len(l)):
            for j in range(len(l)):
                if i == j: continue
                a,b = (l[i], l[j])
                dx = a[0] - b[0]
                dy = a[1] - b[1]
                c = 0
                while a[0] + c * dx >= 0 and a[0] + c * dx < mx and a[1] + c * dy >= 0 and a[1] + c * dy < my:
                    coords.add((a[0] + c * dx, a[1] + c * dy))
                    c += 1
    print(len(coords)) #8.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()