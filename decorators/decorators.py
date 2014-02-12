def dec(fn):
    def wrapper(*args):
        return fn(*args)
    return wrapper

@dec
def foo(a, b, c):
    print a, b, c

if __name__ == "__main__":
    foo(1, 2, 3)
