__author__ = 'young'

# file one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

print 'one : __name__ = ', __name__

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")

