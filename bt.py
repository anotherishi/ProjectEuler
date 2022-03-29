class Node:
    def __init__(self, value):
        self.value = value
        self.l = self.r = None

    def cln(self):
        i = self.l
        c = 0
        while True:
            c += 1
            if not i:
                break
            i = i.l
        return c

    def crn(self):
        i = self.r
        c = 0
        while True:
            c += 1
            if not i:
                break
            i = i.r
        return c

    def pr(self):
        i=self.l
        j=self.r
        sep='+--'
        nm=3
        while 1:
            s= '''
            {self.value}
            {sep}{i}
            '''



n = Node(1)
n.l = Node(2)
n.r = Node(3)

n.l.l = Node(4)
n.l.r = Node(5)

print(n.cln())
print(n.crn())
