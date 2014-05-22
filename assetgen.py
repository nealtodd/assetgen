#!/usr/bin/python

import os
import subprocess
import random

with open('assets.txt') as f:
    with open(os.devnull, "w") as fnull:
        for i, l in enumerate(f, 1):
            try:
                line = l.split(' ')
                in_type = line[0]
                in_file = 'types/type.%s' % in_type
                min_size, max_size, number = map(int, line[1:])
                if os.path.isfile(in_file):
                    for j in xrange(1, number + 1):
                        file_size = random.randrange(min_size, max_size)
                        _ = subprocess.call([
                            'dd',
                            'if=%s' % in_file,
                            'of=%s' % 'assets/asset%s.%s' % (j, in_type),
                            'bs=%s' % file_size,
                            'conv=sync'
                        ], stdout=fnull, stderr=fnull)
                    print "Generated %s %s" % (number, in_type)
                else:
                    print "Line %s: no such file: %s" % (i, in_file)
            except Exception, e:
                print "Line %s: %s" % (i, e)
