r=0

def calc_sum(word: str):
    sum: int = 0
    for letter in word.upper():
        sum += ord(letter) - 64
    return sum

def is_triangle(number: int):
    d=1+8*number
    x1=(-1+d**.5)/2
    return x1==int(x1)

with open('./42_words.txt') as f:
    dt=f.read().replace('"', '').split(',')

for i in dt:
    s=0
    for j in i:
        s+=ord(j)-64
    d=1+8*s
    x1=(-1+d**.5)/2
    if x1==int(x1):
            r+=1

print(r)
r=0

for i in dt:
    if is_triangle(calc_sum(i)):
        r+=1

print(r)