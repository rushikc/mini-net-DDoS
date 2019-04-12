import sys


print sys.argv

ls =sys.argv
ls = ls[1:]
msg=''
for k in ls:
  msg+= k + ' '

