def read_file():
    a = []
    f = open("input04", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def task1(f):
    sum = 0
    rows = len(f)
    cols = len(f[0])
    for y in range(rows):
        for x in range(cols):
            l = f[y][x]
            if l != "X": continue
            if x <= cols-4:
                if f[y][x+1] == "M" and f[y][x+2] == "A" and f[y][x+3] == "S": sum += 1
            if x <= cols-4 and y <= rows-4:
                if f[y+1][x+1] == "M" and f[y+2][x+2] == "A" and f[y+3][x+3] == "S": sum += 1
            if y <= rows-4:
                if f[y+1][x] == "M" and f[y+2][x] == "A" and f[y+3][x] == "S": sum += 1
            if y <= rows-4 and x >= 3:
                if f[y+1][x-1] == "M" and f[y+2][x-2] == "A" and f[y+3][x-3] == "S": sum += 1
            if x >= 3:
                if f[y][x-1] == "M" and f[y][x-2] == "A" and f[y][x-3] == "S": sum += 1
            if x >= 3 and y >= 3:
                if f[y-1][x-1] == "M" and f[y-2][x-2] == "A" and f[y-3][x-3] == "S": sum += 1
            if y >= 3:
                if f[y-1][x] == "M" and f[y-2][x] == "A" and f[y-3][x] == "S": sum += 1
            if y >= 3 and x <= cols-4:
                if f[y-1][x+1] == "M" and f[y-2][x+2] == "A" and f[y-3][x+3] == "S": sum += 1
    print(sum) #4.1

def task2(f):
    sum = 0
    rows = len(f)
    cols = len(f[0])
    for y in range(1, rows-1):
        for x in range(1, cols-1):
            l = f[y][x]
            if l != "A": continue
            set1 = {f[y-1][x-1], f[y+1][x+1]}
            if set1 != {"M", "S"}: continue
            set2 = {f[y-1][x+1], f[y+1][x-1]}
            if set2 == {"M", "S"}: sum += 1
    print(sum) #4.2

def main():
    f = read_file()
    task1(f)
    task2(f)

if __name__== "__main__":
    main()