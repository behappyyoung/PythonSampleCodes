__author__ = 'young'


import one

print("top-level in two.py")
one.func()

print 'importing __name__ = ', __name__

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")
