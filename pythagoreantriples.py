s=set()

for n in range(3, 100):
    m= n/2
    if m==int(m):
        m=int(m)
        a=m**2-1
        b=2*m
        c=m**2+1
        s.add((a,b,c))
    m=(n-1)**.5
    if m==int(m):
        m=int(m)
        a=m**2-1
        b=2*m
        c=m**2+1
        s.add((a,b,c))

print(s, len(s))
