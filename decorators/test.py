def dec(fn):
    def inner(a):
        print "inner"
    return inner


@dec
def myfun(a):
    print "hi"


myfun(1)
