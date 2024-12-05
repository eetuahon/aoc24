def read_file():
    a = []
    f = open("input05", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def format_file(f):
    rules = []
    input = []
    for l in f:
        if "|" in l:
            r = l.split("|")
            rules.append((int(r[0]), int(r[1])))
        elif "," in l:
            input.append([int(i) for i in l.split(",")])
    return (rules, input)

inc = []

def task1(f):
    global inc
    sum = 0
    rules = f[0]
    input = f[1]
    for i in input:
        ok = True
        for r in rules:
            if r[0] not in i or r[1] not in i: continue
            if i.index(r[0]) > i.index(r[1]):
                ok = False
                break
        if ok: sum += i[len(i) // 2]
        else: inc.append(i)
    print(sum) #5.1

def task2(f):
    global inc
    sum = 0
    rules = f[0]
    for i in inc:
        temp = i
        change = False
        while (True):
            for r in rules:
                if r[0] not in i or r[1] not in i: continue
                i1 = temp.index(r[0])
                i2 = temp.index(r[1])
                if i1 > i2:
                    temp.remove(r[0])
                    temp.insert(i2, r[0])
                    change = True
            if change == False:
                break
            change = False
        sum += temp[len(i) // 2]
    print(sum) #5.2

def main():
    f = read_file()
    f = format_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()