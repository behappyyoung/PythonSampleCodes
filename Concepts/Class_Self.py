
class A:
    x = []              # shared by Instances

    def add(self):
        self.x.append(1)


class B:
    def __init__(self):
        self.x = []         # private

    def add(self):
        self.x.append(1)


class C:
    def __init__(s):
        s.x = []         # private

    def add(s):
        s.x.append(1)


x = A()
y = A()
x.add()
y.add()
print("A's x:", x.x)

x = B()
y = B()
x.add()
y.add()
print("B's x:", x.x)

x = C()
y = C()
x.add()
y.add()
print("C's x:", x.x)