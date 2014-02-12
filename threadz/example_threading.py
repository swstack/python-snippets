import threading
import time
import os

mod_lock = threading.Lock()


class MyThread(threading.Thread):
    class_lock = threading.Lock()

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        for _ in xrange(5):
            time.sleep(1)
        print '%s all done.' % self.name

    def acquire_class_lock(self):
        self.class_lock.acquire()

    def release_class_lock(self):
        self.class_lock.release()

t1 = MyThread('t1')
t2 = MyThread('t2')


t1.acquire_class_lock()
t1.release_class_lock()
t2.acquire_class_lock()
t2.release_class_lock()
#for cnt in xrange(5):
#    MyThread(('t%d' % cnt)).start()
