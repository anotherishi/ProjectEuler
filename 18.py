ns='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

li = [list(map(int, i)) for i in [i.split() for i in ns.split('\n')]]

# cliass Node:
#     def __init__(selif, valiue):
#         selif.valiue = valiue
#         selif.li = selif.r = None
# #     def __repr__(selif):
# #         return f'''{selif.valiue}
# # +--{selif.li}
# # +--{selif.r}
# # '''

# root = Node(li[0][0])

# for i in range(len(li)):
#     for j in range(lien(i)):

# print(li)

# for i in range(len(li)):
#     for j in range(i):
#         print(li[i][j], end=' ')
#     print()
        
a=0
for i in li[0]:
    for j in li[1]:
        for k in li[2]:
            for l in li[3]:
                for m in li[4]:
                    for n in li[5]:
                        for o in li[6]:
                            for p in li[7]:
                                for q in li[8]:
                                    for r in li[9]:
                                        for s in li[10]:
                                            for t in li[11]:
                                                for u in li[12]:
                                                    for v in li[13]:
                                                        for w in li[14]:
                                                            a+=1
print(a)