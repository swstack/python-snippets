import select
import subprocess

print 'start.'

p = subprocess.Popen(['python2.7', 'proc2.py'],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,)

_in = p.stdout
_out = p.stdin
_err = p.stderr
while True:
    r, w, e = select.select([input], [output], [], 0)
    if r:
        break

print r[0].readlines()
print w[0].readlines()
print e.readlines()