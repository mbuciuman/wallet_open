#!/usr/bin/env python3
import subprocess
import sys
import re
import itertools
import string
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


def testPass(password):
    bashCommand = "mbexport /home/mbc/Documents/wallet.aes %s" % password
    p = subprocess.Popen(
        bashCommand.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)
    output, error = p.communicate()
    print("Testing password %s" % (password))
    if not re.search(".*bad decrypt.*", error):
        print("DECRYPT FOUND!!! Password: %s" % output)
        return


def main():
    #pool = Pool(processes=100)
    maxsize = 3
    for size in range(0, maxsize):
        print("Testing passwords of size %s, Current time: %s" %
              (size, str(datetime.now())))
        executor = ThreadPoolExecutor(max_workers=10)
        textlist = list(
            map("".join, itertools.product(string.printable, repeat=size)))
        a = executor.map(testPass, textlist)
        #pool.map(testPass, textlist)
        print("Finished testing passwords of size %s, Current time: %s" %
              (size, str(datetime.now())))

if __name__ == "__main__":
    main()
