import subprocess
import struct
import select

print 'start.'

p = subprocess.Popen(['python2.7', 'proc2.py'],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=None
)

while True:
    raw = p.stdout
#    raw = select.select([p.stdout], [], [])[0][0]
    raw = raw.read(1)
    data = struct.unpack(">b", raw)[0]
    if data == -1:
        break
    print data
print 'done.'
