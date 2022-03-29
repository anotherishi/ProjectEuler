from math import sqrt, ceil

def dgnl(n, ds):
    l = [1]
    for i in range(n-1):
        l.append(l[i] + ds)
        ds += 8
    return l

def is_prime(n):
    for i in range(2, ceil(sqrt(n))):
        if not n%i:
            return False
    return True

def all_d(n):
    return set(dgnl(n, 2) + dgnl(n, 4) + dgnl(n, 6)) - {1}


i=2
while True:
    np=len(set(filter(is_prime, all_d(i))))
    tot=(i-1)*4+1
    per = np/tot*100
    print(per)
    if per < 10:
        print(i)
        break
    i+=1

print(dgnl(4,3))