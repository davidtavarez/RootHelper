#!/usr/bin/env python
import requests
import os, errno

folder = "/tmp/"
helpers = [
    ('http://www.securitysift.com/download/linuxprivchecker.py', folder + 'linuxprivchecker.py') , 
    ('https://github.com/rebootuser/LinEnum/archive/master.zip',folder + 'LinEnum.zip'), 
    ('https://github.com/jondonas/linux-exploit-suggester-2/archive/master.zip', folder + 'ExploitSuggest_perl.zip'),
    ('https://github.com/pentestmonkey/unix-privesc-check/archive/1_x.zip', folder + 'unixprivesc'),
    ('https://github.com/craigz28/firmwalker/archive/master.zip', folder + 'firmwalker.zip')
    ('https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh', folder + 'les.sh')
];

for helper in helpers:
    # Frist, we should download the file
    r = requests.get(helper[0], allow_redirects=True)
    with open(helper[1], 'wb') as f:
        f.write(r.content)
    try:
        os.remove(helper[1])
    except OSError, e:
        if e.errno != errno.ENOENT:
            raise 

