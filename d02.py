def read_file():
    a = []
    f = open("input02", "r")
    for i in f:
        if len(i) > 1:
            a.append(i.replace("\n",""))
    f.close()
    return a

def modify_file(f):
    return [[int(i) for i in r.split(" ")] for r in f]

def validIncr(ar):
    for i in range(1, len(ar)):
        if ar[i] - ar[i-1] <= 0 or ar[i] - ar[i-1] > 3: return False
    return True

def validDecr(ar):
    for i in range(1, len(ar)):
        if ar[i] - ar[i-1] >= 0 or ar[i] - ar[i-1] < -3: return False
    return True

def task1(f):
    sum = 0
    for r in f:
        safe = True
        for i in range(1,len(r)):
            d = r[i] - r[i-1]
            if abs(d) > 3 or d == 0:
                safe = False
                break
            if d > 0 and r[1] - r[0] < 0:
                safe = False
                break
            if d < 0 and r[1] - r[0] > 0:
                safe = False
                break
        if safe: sum += 1
    print(sum) #2.1

def task2(f):
    sum = 0
    for r in f:
        if validIncr(r): sum += 1
        elif validDecr(r): sum += 1
        else:
            for i in range(len(r)):
                if validIncr(r[:i]+ r[i+1:]):
                    sum += 1
                    break
                if validDecr(r[:i]+ r[i+1:]):
                    sum += 1
                    break
    print(sum) #2.2

def main():
    f = read_file()
    f = modify_file(f)
    task1(f)
    task2(f)

if __name__== "__main__":
    main()