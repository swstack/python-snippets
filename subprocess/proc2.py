import sys
import struct
import time

time.sleep(10)
for i in range(10):
    sys.stdout.write('%s' % i)
sys.stdout.write(struct.pack(">b", -1))
