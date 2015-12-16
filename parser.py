#!/usr/bin/python
__author__ = 'rahul'
import re
import os
import time
import sys, getopt


def usage():
	print("Usage: %s <filename> <admin> <tenantid>" % sys.argv[0])
        sys.exit(2)

 
regexp='admin'
logLocation="/opt/stack/logs/c-api.log"
total = len(sys.argv)
cmdargs = str(sys.argv)

'''
logfilename='myfile'
adminid='503c7a167f1d4be3b732f92faa3bb9e0'
tenantid='11fb56caaeaa48929943d402a7541491'
'''

if total < 3:
	usage()

inputfile = str(sys.argv[1])


print('total =')
print(total)
print('inputfile ='+inputfile)


for i in xrange(total):
	if i>1:
		regexp+='|'+str(sys.argv[i])
   		print ("Argument # %d : %s" % (i, str(sys.argv[i])))


print regexp


def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def writetofile(line,filename):
        f = open(filename,'a')
        f.write(line) # python will convert \n to os.linesep
        f.close()



if __name__ == '__main__':
    logfile = open(logLocation,"r")
    loglines = follow(logfile)
    for line in loglines:
        print line
        searchObj = re.search( r'.*('+regexp+').*', line, 0)
        if searchObj:
                writetofile(line,inputfile)
