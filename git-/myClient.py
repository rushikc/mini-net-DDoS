import socket, optparse
import sys
parser = optparse.OptionParser()
parser.add_option('-i', dest='ip', default='127.0.0.1')
parser.add_option('-p', dest='port', type='int', default=12345)
parser.add_option('-m', dest='msg')
(options, args) = parser.parse_args()

#print sys.argv

ls =sys.argv
ls = ls[1:]
msg=''
for k in ls:
  msg+= k + ' '

if msg == ' ' or msg== '':
  msg = 'Nothing'
print msg
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(msg.encode('utf-8'), (options.ip, options.port) )
