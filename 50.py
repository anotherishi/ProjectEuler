def is_prime(n):
    for i in range(2, n):
        if not n%i:
            return False
    return True

def gen_prime(upto):
    for i in range(2, upto+1):
        if is_prime(i):
            yield i

l=[]
for i in range(2, 50000):
    if is_prime(i):
        l.append(i)
print(l)


for i in range(1, 30000):
    s=0
    for j in range(i):
        s+=l[j]
    if is_prime(s):
        print(s)
    if s>1000000:
        break