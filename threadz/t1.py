import threading
import time

lock = threading.RLock()


class MyThread(threading.Thread):
    class_lock = threading.Lock()

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print "Running ... %s" % self.name

        print threading.active_count()
        lock.acquire()
        while True:
            time.sleep(2)
        print "Done ... %s" % self.name


def main():
    t1 = MyThread('t1')
    t1.start()
    while True:
        x = raw_input("Enter a command...")
        if x == "1":
            t1.start()

if __name__ == "__main__":
    main()
