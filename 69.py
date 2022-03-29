from math import gcd as hcf


def phi(n):
    c = 1
    for i in range(2, n):
        if hcf(i, n) == 1:
            c += 1
    return n/c

max=0

ni=0

for i in range(2, 1000001):
    new = phi(i)
    if new> max:
        max=new
        ni=i

print(max, i)