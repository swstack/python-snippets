#!/usr/bin/env python

import time
import os
file("/tmp/cronjob.stat", "w").write(os.path.abspath('.'))

for i in xrange(0, 200):
    with open("cron.out", "a") as f:
        f.write("%s\n" % i)
    time.sleep(1)
