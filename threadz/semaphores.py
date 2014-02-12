import threading
from random import randint


class fill_count:
    value = 0


class empty_count:
    value = 10


fill_cnt = fill_count()
empty_cnt = empty_count()

buf = []
buf_upper_bound = 10

wakeup = threading.Event()


def _item():
    return randint(0, 100)


def _down(count):
    if count.value == 0:
        print "Thread --> %s <-- going to sleep" % threading.currentThread().getName()
        wakeup.wait()
    else:
        count.value -= 1


def _up(count):
    count.value += 1


def producer():
    global fill_cnt, empty_cnt

    while True:
        item = _item()
        _down(empty_cnt)
        buf.append(item)
        _up(fill_cnt)


def consumer():
    global fill_cnt, empty_cnt

    def _consume(item):
        wakeup.set()
        wakeup.clear()

    while True:
        _down(fill_cnt)
        item = buf.pop()
        _up(empty_cnt)
        _consume(item)


if __name__ == "__main__":
    p = threading.Thread(target=producer, name="Producer")
    c = threading.Thread(target=consumer, name="Consumer")
    c.start()
    p.start()
