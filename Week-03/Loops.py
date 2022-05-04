class Voxel:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.c = 7

    def sum(self):
        return self.a + self.b + self.c

    def printed(self):
        print("hello")

v = Voxel(1,2)
result = v.sum()
print("result...",result)
print(v.printed())