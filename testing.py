import sys
print(sys.executable)
print(sys.version)

for num in [1, 2, 3, 4]:
    print(num)

for numer in [12, 3, 14, 15]:
    print(numer)


class ClassName(object):
    """docstring for ClassName"""

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
