#!/usr/bin/python

import sys
import os
import subprocess

args = sys.argv

if len(args[1:]) and os.path.isfile(args[1]):
    try:
        bytes = int(args[2])
    except:
        bytes = 10
    in_type = subprocess.check_output(['file', args[1]])
    out_file = 'types/type.%s' % args[1].split('.')[-1]
    with open(os.devnull, "w") as fnull:
        subprocess.call([
            'dd',
            'if=%s' % args[1],
            'of=%s' % out_file,
            'bs=%s' % bytes,
            'count=1'
        ], stdout=fnull, stderr=fnull)
    out_type = subprocess.check_output(['file', out_file])

    print 'Input type:\n\t%s\nOutput type:\n\t%s' % (in_type, out_type)
