# f = open("bajrang.txt")
# # content = f.read()
# # print(content)
# for line in f:
#     print(line, end="")

# f.close()



# import random

# print(random.__doc__)

class distance:
    def __init__(self, x=None,y=None):
        self.ft=x
        self.inch=y
    def __ge__(self, x):
        val1=self.ft*12+self.inch
        val2=x.ft*12+x.inch
        if val1>=val2:
            return True
        else:
            return False
d1=distance(2,1)
d2=distance(4,10)
c= d1>=d2
print(c)